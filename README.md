# 🎓 EduTrack Pro - Student Management System

EduTrack Pro is a modern, feature-rich **Student Management System** built using **Django** and **MongoDB**. It provides an intuitive and highly professional User Interface (UI) to efficiently manage students, classes, and daily attendance.

---

## 🚀 Key Features

* **📊 Interactive Dashboard:** Provides a quick overview of the total number of students, classes, and attendance records.
* **👨‍🎓 Student Management (CRUD):** Add, View, Edit, and Delete student records with ease.
* **🏫 Class Management:** Create and organize classes with academic years and sections.
* **📅 Attendance Tracking:** Mark daily attendance (Present/Absent) with a smart student dropdown.
* **📈 Attendance Reports:** Automatically calculates the total attendance percentage for individual students.
* **🔍 Search Functionality:** Easily search for students by name.
* **🎨 Professional UI/UX:** Clean, modern, responsive design using custom CSS with shadow effects, cards, and interactive hover states.

---

## 🛠️ Technology Stack

* **Backend:** Python, Django 4.1
* **Database:** MongoDB (via `djongo` engine)
* **Frontend:** HTML5, CSS3 (Custom responsive design)
* **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```text
student_management_system/
│
├── manage.py
├── .env
├── requirements.txt
│
├── student_project/        # Main Django Configuration
│   ├── settings.py
│   ├── urls.py
│   └── views.py            # Dashboard view
│
├── apps/                   # App Modules
│   ├── students/           # Student CRUD & Search
│   ├── classes/            # Class CRUD
│   └── attendance/         # Attendance tracking & Reports
│
├── templates/              # HTML Templates
│   ├── base.html           # Main UI Layout & Navbar
│   ├── dashboard.html      # Overview Cards
│   ├── students/
│   ├── classes/
│   └── attendance/
│
└── static/
    └── css/
        └── style.css       # Custom Professional Styling
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone <repository-url>
cd student_management_system
```

### 2. Create a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
Make sure you have all required packages (Django, djongo, pymongo, python-dotenv, pytz).
```bash
pip install django djongo pymongo python-dotenv pytz
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory and add your MongoDB connection details:
```env
MONGO_URL=mongodb://127.0.0.1:27017
MONGO_DB_NAME=student_db
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Server
```bash
python manage.py runserver
```

Open your browser and navigate to: `http://127.0.0.1:8000/`

---

## 👨‍💻 Author

Developed as a modern full-stack web application for efficient school administration.
