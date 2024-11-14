# Django Template

This repository serves as a basic template for quickly setting up a Django project with environment variables and structured project folders.

## Features

- Pre-configured `.env` file for environment variables.
- Basic project structure for a Django app with `api` module.
- Easy-to-install dependencies via `requirements.txt`.
- A guide for generating a secret key and running the Django server.


## Getting Started


### 1. Clone the Repository
```bash
git clone https://github.com/shaheem-pp/django-template.git
cd django-template
```


### 2. Set Up Environment Variables

Create a `.env` file in the project directory and populate it with your project-specific values:
```env
SECRET_KEY=YOUR_KEY_HERE
DEBUG=YOUR_KEY_HERE
ALLOWED_HOSTS=YOUR_KEY_HERE
DB_ENGINE=YOUR_KEY_HERE
DB_NAME=YOUR_KEY_HERE
DB_USER=YOUR_KEY_HERE
DB_PASSWORD=YOUR_KEY_HERE
DB_HOST=YOUR_KEY_HERE
DB_PORT=YOUR_KEY_HERE
TIME_ZONE=YOUR_KEY_HERE
USE_TZ=YOUR_KEY_HERE
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Generate a Secret Key

Run the following command in your Python shell to generate a new `SECRET_KEY`:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```


### 5. Run Migrations and Start the Server

```bash
python manage.py migrate
python manage.py runserver
```


## Project Structure

```text
.
├── README.md
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt

4 directories, 16 files
```

## Contributing

Feel free to contribute by submitting a pull request.


## Author

- **Shaheem P P** - [LinkedIn](https://www.linkedin.com/in/shaheem-pp/) [Website](https://shaheem.netlify.app/)
