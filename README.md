# 📝 Daily Journal Web Application

A secure, feature-rich, and beautifully designed journaling platform built with Python and Flask.  
It allows users to document their thoughts, experiences, and reflections with a focus on security, usability, and elegant design.

---

## ✨ Features

- **Google OAuth Authentication**
  - Secure login with Google accounts (Authlib integration)
- **Full Journal Management (CRUD)**
  - Create, Read, Update, and Delete journal entries
  - Live Markdown editor with real-time preview
- **Calendar View**
  - Visual calendar to browse journal entries by date
- **Search Functionality**
  - Search journal entries by keywords
- **Responsive & Modern UI**
  - Mobile-friendly, clean, and minimal interface
- **Dark/Light Mode Toggle**
  - User-friendly theme switcher for eye comfort
- **Profile Picture Proxy Loading**
  - Lazy and secure proxy loading of Google profile pictures
- **Flash Messaging**
  - Success and error alerts with auto-dismiss animation
- **Custom Error Pages**
  - Beautiful 404 and 500 error pages
- **Security Enhancements**
  - CSRF protection on all forms
  - Secure session cookie settings (`HttpOnly`, `SameSite=Lax`)

---

## 🛠️ Technologies Used

- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript
- **Templating Engine:** Jinja2
- **Authentication:** Google OAuth 2.0 (Authlib)
- **Forms and Validation:** Flask-WTF
- **Database:** SQLite (Development) — easily switchable to PostgreSQL/MySQL

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/daily-journal.git
cd daily-journal
