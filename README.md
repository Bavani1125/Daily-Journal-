# 📝 Daily Journal Web Application

A secure, feature-rich, and beautifully designed journaling platform built with Python and Flask.  
It allows users to document their thoughts, experiences, and reflections with a focus on security, usability, and elegant design.

---

## ✨ Features![WhatsApp Image 2025-05-20 at 8 16 48 AM](https://github.com/user-attachments/assets/1ef0b667-521e-4459-adc0-dea7c30bc40d)
![WhatsApp Image 2025-05-20 at 8 16 04 AM](https://github.com/user-attachments/assets/57369070-7a17-45ea-b625-7006913480c1)
![WhatsApp Image 2025-05-20 at 8 13 36 AM](https://github.com/user-attachments/assets/93ac7465-795d-46a4-a86e-b90efcc32899)
![WhatsApp Image 2025-05-20 at 8 11 52 AM](https://github.com/user-attachments/assets/88d763de-7156-4df5-8585-5cc952cb5ed6)


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
