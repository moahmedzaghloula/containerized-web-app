# Containerized Web Application for Book Management

This project is a **containerized web application** that allows users to manage a collection of books. It uses **FastAPI** for the backend API, **PostgreSQL** for database management, and **Redis** for caching. The application is fully containerized using **Docker Compose**, allowing easy setup and deployment.

The app also uses **Nginx** as a reverse proxy to handle requests and forward them to the FastAPI backend.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Docker Setup](#docker-setup)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This web application provides a RESTful API for managing books. It supports two main operations:

1. **List Books**: Get a list of books stored in the database.
2. **Add Book**: Add a new book to the database.

The app is designed to be fast and efficient by utilizing **Redis caching** for frequently accessed data, ensuring that repeated requests for the same information are served from cache, reducing database load.

---

## Features

- **Book Management**: Allows adding and retrieving books (title, author, year).
- **Database Integration**: Uses **PostgreSQL** for storing book data.
- **Caching**: Caches book list in **Redis** to speed up retrieval.
- **Dockerized**: Fully containerized application for easy deployment and scalability.
- **Reverse Proxy**: **Nginx** is used as a reverse proxy to route requests to the backend.
- **Asynchronous Programming**: Fast and responsive API using FastAPI and asynchronous Redis client.

---

## Technologies

- **FastAPI**: Web framework for building APIs.
- **PostgreSQL**: Relational database to store book data.
- **Redis**: In-memory data store used for caching.
- **Nginx**: Reverse proxy to handle requests.
- **Docker**: Containerization of the application using Docker Compose.

---

## Docker Setup

This project uses **Docker Compose** to orchestrate the containers. The following services are defined in the `docker-compose.yml` file:

- **app**: FastAPI application container.
- **db**: PostgreSQL database container.
- **redis**: Redis cache container.
- **nginx**: Nginx reverse proxy container.

### To build and start the containers, run the following command:

```bash
docker-compose up --build
