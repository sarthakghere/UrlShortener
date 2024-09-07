# URL Shortener API

This Django project provides an API for shortening URLs. It allows you to shorten a long URL, retrieve the original URL from a short code, update an existing short URL, and delete a short URL.

## Features

- **Shorten URL**: Generate a short code for a given URL.
- **Retrieve URL**: Get the original URL from a short code.
- **Update Shorten URL**: Modify the original URL associated with a short code.
- **Delete URL**: Remove a short code and its associated URL.
- **Redirect to Original URL**: Redirects user to the original URL associated with a short code.


## Technologies

- Django
- Django REST Framework
- Python
- SQLite (or any other database of your choice)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sarthakghere/UrlShortener.git
   cd UrlShortener
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

- **Endpoint:** `/shorten/`
- **Method:** `POST`
- **Example Request Body:** 
  ```json
  {
    "url": "https://www.github.com"
  }
  ```
- **Response:**
  ```json
  {
    "id": 12,
    "short_code": "gzLIfv",
    "url": "https://www.github.com",
    "createdAt": "2024-09-07T17:11:10.950152Z",
    "updatedAt": "2024-09-07T17:11:10.950211Z"
  }
  ```

### Retrieve URL

- **Endpoint:** `/shorten/<short_code>/`
- **Method:** `GET`
- **Example Request URL:**
  ```json
  /retrieve/gzLIfv/
  ```
- **Response:**
  ```json
  {
    "id": 12,
    "short_code": "gzLIfv",
    "url": "https://www.github.com",
    "createdAt": "2024-09-07T17:11:10.950152Z",
    "updatedAt": "2024-09-07T17:11:10.950211Z"
  }
  ```

### Update URL

- **Endpoint:** `/shorten/<short_code>/`
- **Method:** `PUT`
- **Example Request Body:**
  ```json
  {
    "updated_url" : "https://google.com"
  }
  ```
- **Response:**
  ```json
  {
    "id": 12,
    "short_code": "gzLIfv",
    "url": "https://google.com",
    "createdAt": "2024-09-07T17:11:10.950152Z",
    "updatedAt": "2024-09-07T17:14:42.836037Z"
  }
  ```

### Stats URL

- **Endpoint:** `/shorten/<short_code>/stats/`
- **Method:** `GET`
- **Example Request URL:**
  ```text
  /shorten/gzLIfv/stats
  ```
- **Response:**
  ```json
  {
    "id": 12,
    "short_code": "gzLIfv",
    "url": "https://google.com",
    "createdAt": "2024-09-07T17:11:10.950152Z",
    "updatedAt": "2024-09-07T17:19:44.684297Z",
    "accessCount": 1
  }
  ```



### Delete URL

- **Endpoint:** `/delete/<short_code>/`
- **Method:** `DELETE`
- **Example Request URL:**
  ```text
  /delete/gzLIfv/
  ```
- **Response Code:** 204 No Content
  



