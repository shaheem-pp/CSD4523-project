# About ReciMe

**ReciMe** is a collaborative recipe-sharing platform built as part of the **final project** for the course **2024F CSD
4523 6 Python II**.

### Developed by

1. **Hardee Manishkumar Raval (C0946490)**
2. **Thrisha Selvaraj (C0941392)**
3. **Shaheem Puzhuthini Para (C0935469)**

This app is designed to bring food lovers, aspiring chefs, and culinary experts together in one vibrant community.

### URL

[YouTube - Presentation](URL)

### Key Features:

1. **Discover Recipes**: Explore a wide variety of recipes with detailed instructions, ingredients, and optional images
   to inspire your next meal.
2. **Create Your Own Recipes**: Users can contribute their unique recipes and share their love for cooking with the
   community.
3. **Engage With Content**: Like and bookmark recipes you love for quick access later, and leave thoughtful reviews to
   guide others.
4. **Chef Mode**: A dedicated space for chefs to shine! Chefs can create high-quality content, and their reviews are
   featured at the top, ensuring credibility and expert insights.
5. **Interactive Community**: ReciMe promotes collaboration and engagement among users, offering an inclusive platform
   for food enthusiasts of all levels.

### Why ReciMe?

ReciMe is not just about recipes—it's about creating a community where people can share their culinary adventures, learn
from each other, and celebrate their love for food. Whether you’re a casual cook, an experimental foodie, or a
professional chef, ReciMe has something to offer.

This project highlights the effective use of Django to create a full-stack web application with engaging features like
user interaction, bookmarking, chef-curated content, and community-driven feedback.

We hope ReciMe becomes your go-to app for sharing and discovering recipes. Bon appétit!

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shaheem-pp/CSD4523-project.git
cd CSD4523-project
```

### 2. Set Up Environment Variables

Create a `.env` file in the project directory and Setup like below:

```env
SECRET_KEY=Your Django project's secret key (use the generated key)
DEBUG=True or False (set True for local development)
ALLOWED_HOSTS=Comma-separated list of allowed hostnames
USE_TZ=True or False (whether to enable timezone support)
TIME_ZONE=Your timezone (e.g., America/Toronto)
```

### 3. Generate a Secret Key

Run the following command in your Python shell to generate a new `SECRET_KEY`:

```python
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
``` 

### 5. Run Migrations, Collect static and Start the Server

```bash
python manage.py migrate
python manage.py collectstatic #should do this for rendering WYSIWYG Editor
python manage.py runserver
```

## Project Structure

```text
.
├── README.md
├── __pycache__
├── appAuth/
├── appRecipe/
├── appUser/
├── assets/
├── customUtils.py
├── db.sqlite3
├── manage.py
├── media/
├── project/
├── requirements.txt
├── staticfiles/
└── templates/

10 directories, 5 files

```