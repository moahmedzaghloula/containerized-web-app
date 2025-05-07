from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from contextlib import contextmanager
import redis.asyncio as redis
import atexit

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int

@contextmanager
def get_db():
    conn = psycopg2.connect(
        dbname="book_db",
        user="postgres",
        password="example",
        host="db",
        port="5432"
    )
    try:
        yield conn
    finally:
        conn.close()

def get_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, year FROM books")
    return [{"title": row[0], "author": row[1], "year": row[2]} for row in cursor.fetchall()]

def create_book(conn, book: Book):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)",
        (book.title, book.author, book.year)
    )
    conn.commit()

redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.get("/books")
async def list_books():
    cached_books = await redis_client.get("books")
    if cached_books:
        return {"books": eval(cached_books.decode())}
    with get_db() as conn:
        books = get_books(conn)
        await redis_client.set("books", str(books), ex=3600)
        return {"books": books}

@app.post("/books")
async def add_book(book: Book):
    with get_db() as conn:
        create_book(conn, book)
        await redis_client.delete("books")
        return {"message": "Book added successfully"}

atexit.register(lambda: redis_client.close())