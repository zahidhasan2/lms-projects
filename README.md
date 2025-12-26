

## Project Structure
lms-project/
├─ README.md
├─ lms-backend/
│ ├─ manage.py
│ ├─ requirements.txt
│ ├─ lms_backend/
│ │ ├─ settings.py
│ │ └─ urls.py
│ ├─ accounts/ # auth, users, roles
│ │ ├─ models.py # custom User with role
│ │ ├─ serializers.py
│ │ ├─ permissions.py
│ │ ├─ tokens.py
│ │ ├─ views.py
│ │ └─ urls.py
│ └─ lms/ # LMS features
│ ├─ models.py # CourseCategory, Course, Enrollment
│ ├─ serializers.py
│ ├─ permissions.py
│ ├─ reports.py # dashboard stats
│ ├─ views.py
│ └─ urls.py
│
└─ lms-frontend/
├─ package.json
├─ public/
└─ src/
├─ api/axiosClient.js
├─ context/AuthContext.js
├─ components/
│ ├─ Navbar.js
│ └─ ProtectedRoute.js
└─ pages/
├─ LoginPage.js
├─ RegisterPage.js
├─ ForgotPasswordPage.js
├─ ResetPasswordPage.js
├─ ProfilePage.js
├─ CoursesPage.js
├─ CourseDetailPage.js
├─ InstructorCoursesPage.js
└─ AdminDashboardPage.js


---

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
