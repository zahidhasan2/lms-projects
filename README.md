
## Backend Setup (Django + DRF)

cd lms-backend
python -m venv venv
source\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Frontend Setup (React)
cd lms-frontend
npm install
npm start


https://github.com/zahidhasan2/lms-projects/blob/f1f3828fb9accef160acfcee7e5704d8918fb0da/Screenshot%202025-12-26%20192956.png
