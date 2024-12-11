### 1. Clone the Repository
```bash
git clone https://github.com/shaheem-pp/CSD4523-project.git
cd CSD4523-project
```


### 2. Set Up Environment Variables

Create a `.env` file in the project directory and populate it with your project-specific values:
```env
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=YOUR_DEBUG
ALLOWED_HOSTS=YOUR_ALLOWED_HOSTS
USE_TZ=YOUR_USE_TZ
TIME_ZONE=YOUR_TIME_ZONE
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
├── appAuth/
├── appRecipe/
├── appUser/
├── assets/
├── customUtils.py
├── db.sqlite3
├── manage.py
├── media/
├── project/
└── requirements.txt

8 directories, 5 files
```

## Author
1. Hardee Manishkumar Raval - C0946490
2. Thrisha Selvaraj - C0941392
3. Shaheem Puzhuthini Para - C0935469
