# 🎓 EduTrack Pro - Student Management System

EduTrack Pro is a modern, fully functional **Student Management System** built with **Django** and **MongoDB**. It offers a professional dashboard UI, role-based access control, and a complete workflow for managing students, classes, attendance, and reports.

---

## 🚀 Key Features

* **📊 Dashboard Overview:** Shows totals for students, classes, and attendance records in a clean dashboard.
* **👨‍🎓 Student Management:** Add, view, edit, and delete student records.
* **🏫 Class Management:** Add academic classes with year and section.
* **📅 Attendance Tracking:** Mark daily attendance using student dropdowns.
* **📈 Attendance Reports:** View overall attendance summary and student-specific reports.
* **🔐 Role-based Access:** Supports Admin and Teacher roles with proper authorization.
* **🔍 Search Functionality:** Search students by name in the student list.
* **🎨 Custom UI:** Responsive HTML/CSS design with cards, shadows, and modern spacing.

---

## 🛠️ Technology Stack

* **Backend:** Python, Django 4.1
* **Database:** MongoDB via `djongo`
* **Frontend:** HTML5, CSS3 (Custom responsive styles)
* **Config:** `python-dotenv`

---

## 📂 Project Structure

```text
student_management_system/
│
├── manage.py
├── .env
├── requirements.txt
│
├── student_project/        # Django project settings and URLs
│   ├── settings.py
│   ├── urls.py
│   └── views.py            # Dashboard, login, logout
│
├── apps/                   # Django apps
│   ├── students/           # Student CRUD, search, authorization
│   ├── classes/            # Class creation and listing
│   └── attendance/         # Attendance marking and reporting
│
├── templates/              # HTML templates
│   ├── base.html           # Layout, sidebar, dashboard shell
│   ├── dashboard.html      # Dashboard overview page
│   ├── error.html          # Styled access denied page
│   ├── students/
│   ├── classes/
│   └── attendance/
│
└── static/
    └── css/
        └── style.css       # Project-wide styling
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone <repository-url>
cd student_management_system
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install django djongo pymongo python-dotenv pytz
```

### 4. Configure environment variables
Create a `.env` file in the project root with your MongoDB settings:
```env
MONGO_URL=mongodb://127.0.0.1:27017
MONGO_DB_NAME=student_db
```

### 5. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the development server
```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

---

## 🧑‍🏫 Role Setup

Use Django Admin to create roles and assign users:

1. Go to `http://127.0.0.1:8000/admin/`
2. Create a `Teacher` group
3. Assign the teacher user to the `Teacher` group
4. Use admin users for full access

---

## 👨‍💻 Notes

* The app supports role-based access for Admin and Teacher users.
* Reports are available from the attendance section.
* The UI uses custom CSS only—no Bootstrap.

---

## 👨‍💻 Author

Developed as a modern full-stack school administration application.
