
A full-stack web application for managing autonomous robot food delivery.
Built with **Django REST Framework** (backend) and **React** (frontend).

---

## Architecture Overview

```
Maxx-Byte-Food-Delivery/
├── backend/                   Django + DRF + Django Channels
│   ├── config/                Settings, URLs, ASGI/WSGI
│   │   ├── urls.py             contains root url patterns i.e.(api/ & admin/)
│   └── apps/
│   │   ├── models/             contains models for db that include ordering, items, payment, etc.
│   │   ├── views/              contains api endpoints handling
│   │   ├── urls.py             contains url patterns
│   │ 
│   └── robot_delivery/
│        └──  tests/           contains tests
│                │
│                ├── api/      contains tests for api endpoints
│                │
│                └── model/    contains tests for models     
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
pytest robot_delivery tests
```
<h3>To run API or Model tests only</h3>
<h4>Model Tests</h4>

run
```
pytest robot_delivery tests/model
```

<h4>API Tests</h4>

run
```
pytest robot_delivery tests/api
```

<h4>Specific Model Tests</h4>

run
```
pytest robot_delivery tests/model/[file name]
```

<h4>Specific API Tests</h4>

run
```
pytest robot_delivery tests/api/[folder name i.e. orders]/[file name]
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

| POST   | `/api/users/register/` | User registration endpoint <br>

| GET    | `/api/users/<int:user_id>/orders/view_history/` | User order history endpoint <br>

| GET    | `/api/users/<int:user_id>/orders/view_history/item/<int:id>/` | User order history items endpoint <br>

| GET    | `/api/users/<int:user_id>/orders/reorder/<int:id>/` | Reorder from order history endpoint <br>

| GET    | `/api/all_products/`  | All products available endpoint <br>

| POST   | `api/checkout/`  | Create checkout session endpoint <br>