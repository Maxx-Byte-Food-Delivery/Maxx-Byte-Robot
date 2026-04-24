
A full-stack web application for managing autonomous robot food delivery.
Built with **Django REST Framework** (backend) and **React** (frontend).

---

## Architecture Overview

```
Maxx-Byte-Food-Delivery/
├── backend/                   Django + DRF + Django Channels
│   ├── config/                Settings, URLs, ASGI/WSGI
│   └── apps/
│   │
│    └── users/
│        └──  tests/           contains tests
│                └── users/    tests for users
│                │
│                └── model/    contains tests │for models     
│
│ logic
│    └── views/
│        ├── views.py    contains api endpoints handling
│
└── frontend/                  React 19 using Vite
    └── src/
        └──        Various files containg jsx pages such as login
```

---

# Backend:  http://localhost:8000
# Frontend: http://localhost:5173/
# Django Admin: http://localhost:8000/admin/


## Manual Setup

### Backend

Mac: 

```
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Windows:
```
cd backend
python -m venv .venv
```
Command Prompt:
```
.venv\Scripts\activate.bat
```
PowerShell:
```
.\.venv\Scripts\Activate.ps1
```
To install dependencies run
```
pip install -r requirements.txt
```

# Configure environment
cp .env.example .env   # edit DB / Redis credentials

For setting up the database run:
```
python setup_auth.py
python setup_db.py
python manage.py migrate
```
To start backend server run:
```
python manage.py runserver
```


<h3>Running test</h3>
Tests use pytest
to run all tests:

```
cd backend
```
run
```
pytest users
```
### Frontend

```bash
cd frontend
npm install
npm run dev          #http://localhost:5173/
```

---

## User Roles


## Key API Endpoints

| Method | Endpoint                         | Description                    |
|--------|----------------------------------|--------------------------------|

| POST   | `/api/users/login/` |  User login endpoint <br>

| POST   | `/api/users/login/` | User registration endpoint <br>
