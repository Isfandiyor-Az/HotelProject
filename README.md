# 🏨 Hotel Management Website

This repository contains a **Hotel Management Website** developed using **Python (Django framework)**. The project provides a **user-friendly interface** for hotel bookings and management, allowing users to **sign up, log in, browse available rooms, and book accommodations** efficiently.

## ✨ Features

- ✅ **User Authentication** – Sign up, log in, and log out functionality.
- ✅ **Hotel Room Management** – Browse available rooms with details.
- ✅ **Booking System** – Users can book rooms and manage reservations.
- ✅ **Responsive UI** – Styled with HTML, CSS, and Bootstrap.
- ✅ **Media Upload** – Supports images for rooms and hotel-related media.
- ✅ **Database Integration** – Uses SQLite3 for storing user and booking data.

## 🛠️ Tech Stack

- **Backend:** Python (Django) 🐍
- **Frontend:** HTML, CSS, Bootstrap 🎨
- **Database:** SQLite3 🗄️
- **Version Control:** Git & GitHub 🌍

## 📂 Project Structure
📦 Hotel Management Website
│-- 📁 hotel_project/ # Main Django project directory
│-- 📁 hotel/ # Django app handling hotel functionalities
│-- 📁 templates/ # HTML templates for UI
│-- 📁 static/ # Static files (CSS, JS, Images)
│-- 📁 media/images/ # Uploaded images for hotel rooms
│-- 📄 manage.py # Django project management script
│-- 📄 db.sqlite3 # Database file
│-- 📄 README.md # Project documentation

## 🏗️ Future Enhancements
🔹 Add payment integration for online bookings 💳
🔹 Implement admin panel for hotel staff 🛎️
🔹 Improve UI/UX with animations and better styles 🎨

## 🔑 Admin Panel Login Details
For logging into the admin panel:
Username: Admin
Password: 1212


## 🚀 Installation & Setup

Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/hotel-management.git
cd hotel-management


### 2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

 ### 3️⃣Install Dependencies
pip install -r requirements.txt

### 4️⃣ Run Database Migrations
python manage.py migrate
5️⃣ Start the Server
python manage.py runserver
