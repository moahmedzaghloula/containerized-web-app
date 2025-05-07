# Book List Web Application

A production-ready containerized web application built with FastAPI, PostgreSQL, Redis, Nginx, and Docker Compose.

## Setup
1. Install Docker and Docker Compose.
2. Clone the repository: `git clone <your-repo-url>`.
3. Navigate to the project directory: `cd containerized-web-app`.
4. Run `docker-compose up --build`.
5. Access the app at `http://localhost/books`.

## Usage
- **GET `/books`**: Retrieve all books.
- **POST `/books`**: Add a new book (e.g., `{"title": "Book Title", "author": "Author Name", "year": 2023}`).

## Technologies
- FastAPI
- PostgreSQL
- Redis
- Nginx
- Docker Compose

## Database Initialization
Run the following SQL in the PostgreSQL container to create the `books` table:
```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INTEGER NOT NULL
);
