# URL Shortener API

This Django project provides an API for shortening URLs. It allows you to shorten a long URL, retrieve the original URL from a short code, update an existing short URL, and delete a short URL.

## Features

- **Shorten URL**: Generate a short code for a given URL.
- **Retrieve URL**: Get the original URL from a short code.
- **Update URL**: Modify the original URL associated with a short code.
- **Delete URL**: Remove a short code and its associated URL.

## Technologies

- Django
- Django REST Framework
- Python
- PostgreSQL (or any other database of your choice)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Shorten URL

- **Endpoint:** `/api/shorten/`
- **Method:** `POST`
- **Request Body:** 
  ```json
  {
    "url": "http://example.com"
  }
  ```
- **Response:**
  ```json
  {
    "short_code": "abc123",
    "shortened_link": "http://127.0.0.1:8000/abc123"
  }
  ```

### Retrieve URL

- **Endpoint:** `/api/retrieve/`
- **Method:** `GET`
- **Request Body:**
  ```json
  {
    "short_code": "abc123"
  }
  ```
- **Response:**
  ```json
  {
    "id" : 1,
    "short_code": "abcd1234",
    "original_link": "http://example.com",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "accessed": 10
  }
  ```

### Update URL

- **Endpoint:** `/api/update/`
- **Method:** `PATCH`
- **Request Body:**
  ```json
  {
    "short_code": "abc123",
    "updated_url": "http://newexample.com"
  }
  ```
- **Response:**
  ```json
  {
    "id" : 1,
    "short_code": "abcd1234",
    "original_link": "http://example.com",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "accessed": 0
  }
  ```

### Delete URL

- **Endpoint:** `/api/delete/`
- **Method:** `DELETE`
- **Request Body:**
  ```json
  {
    "short_code": "abc123",
  }
  ```
- **Response:**
  ```json
  {
    "message": "Short link deleted"
  }
  ```



