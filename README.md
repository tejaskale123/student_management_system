<div align="center">
  <h1>🎓 EduTrack Pro</h1>
  <p><b>A Next-Generation Student Management System</b></p>
  <p>Built with Django & MongoDB</p>
</div>

---

## 🌟 Overview

**EduTrack Pro** is a modern, responsive, and robust full-stack web application designed for schools and educational institutions. It provides a highly premium SaaS-like UI to manage students, academic classes, attendance records, and generate insights—all powered by a secure Django backend with a NoSQL MongoDB database.

---

## ✨ Key Features

- 📊 **Smart Dashboard** - Get a bird's-eye view of your institution with key metrics for total students, classes, and attendance.
- 👨‍🎓 **Student Management** - Complete CRUD operations for students with a clean UI.
- 🏫 **Class Management** - Organize your school academically with year and section mapping.
- 📅 **Attendance Tracking** - Seamless daily attendance marking with intuitive interfaces.
- 📈 **Comprehensive Reports** - Generate and view attendance reports dynamically.
- 🔐 **Role-Based Access Control (RBAC)** - Secure authorization separating `Admin` and `Teacher` workflows.
- 🎨 **Premium UI/UX** - A completely custom-built interface featuring glassmorphism, smooth animations, and responsive design (No Bootstrap needed).

---

## 🛠️ Technology Stack

**Frontend**
- HTML5 & CSS3 (Custom SaaS-style UI)
- Google Fonts (Inter & Poppins)
- FontAwesome Icons
- Vanilla JavaScript for micro-interactions

**Backend**
- Python 3.x
- Django 4.1 Framework

**Database & Config**
- MongoDB (via `djongo` engine)
- `python-dotenv` for environment management

---

## 📂 Project Architecture

```text
student_management_system/
│── apps/                   # Core Django Applications
│   ├── attendance/         # Attendance & Reports module
│   ├── classes/            # Class & Academic structure module
│   └── students/           # Student Management module
│── student_project/        # Main Django Project Config
│── templates/              # Premium HTML Views
│   ├── base.html           # Main App Shell & Sidebar
│   ├── login.html          # Glassmorphism Login UI
│   └── dashboard.html      # Analytics Dashboard
│── static/                 # Static Assets
│   ├── css/style.css       # Core Design System
│   └── images/             # Backgrounds & Icons
│── .env                    # Environment Variables
└── manage.py               # Django Entry Point
```

---

## 🚀 Quick Start Guide

Follow these instructions to get EduTrack Pro running on your local machine.

### 1. Clone the Repository
```bash
git clone <repository-url>
cd student_management_system
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django djongo pymongo python-dotenv pytz
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
MONGO_URL=mongodb://127.0.0.1:27017
MONGO_DB_NAME=student_db
```

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Start the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 🛡️ Role Setup (Teachers vs Admins)

To enable RBAC, set up groups via the Django Admin panel:
1. Navigate to `http://127.0.0.1:8000/admin/`
2. Create a new Group named **`Teacher`**.
3. Create user accounts for your staff and assign them to the `Teacher` group.
4. Admins (Superusers) inherently have full access to all modules.

---

## 👨‍💻 Developer Notes
- This project utilizes **Djongo** to map Django's ORM seamlessly to MongoDB. Ensure your MongoDB service is running locally or provide a valid Atlas URI in `.env`.
- UI customizations are isolated in `style.css` and internal `<style>` tags for components like the Sidebar and Login pages.

---
<div align="center">
  <p>Crafted with ❤️ for modern education management.</p>
</div>
