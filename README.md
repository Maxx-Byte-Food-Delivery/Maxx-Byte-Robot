
A full-stack web application for managing autonomous robot food delivery.
Built with **Django REST Framework** (backend) and **React** (frontend).

---

## Architecture Overview

```
Maxx-Byte-Robot/
│
├── backend/
│   │
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── apps/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── users/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models/
│   │   │   │   ├── __init__.py
│   │   │   │   └── profile.py
│   │   │   │
│   │   │   ├── migrations/
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── serializers/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── login_serializer.py
│   │   │   │   └── profile_serializer.py
│   │   │   │
│   │   │   ├── views/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── login.py
│   │   │   │   ├── logout.py
│   │   │   │   ├── user_profile.py
│   │   │   │   ├── setup_totp.py
│   │   │   │   ├── verify_totp.py
│   │   │   │   ├── verify_sms.py
│   │   │   │   ├── enable_sms_2fa.py
│   │   │   │   ├── disable_2fa.py
│   │   │   │   └── csrf.py
│   │   │   │
│   │   │   ├── urls.py
│   │   │   │
│   │   │   ├── utils/
│   │   │   │   ├── send_sms.py
│   │   │   │   └── twofa.py
│   │   │   │
│   │   │   └── signals.py
│   │   │
│   │   ├── orders/
│   │   │   ├── __init__.py
│   │   │   ├── models/
│   │   │   │   ├── order.py
│   │   │   │   └── order_item.py
│   │   │   │
│   │   │   ├── views/
│   │   │   │   ├── order_history.py
│   │   │   │   ├── order_tracking.py
│   │   │   │   └── order_cancel.py
│   │   │   │
│   │   │   ├── serializers/
│   │   │   └── urls.py
│   │   │
│   │   ├── products/
│   │   │   ├── __init__.py
│   │   │   ├── models/
│   │   │   │   └── product.py
│   │   │   │
│   │   │   ├── views/
│   │   │   │   └── products.py
│   │   │   │
│   │   │   ├── serializers/
│   │   │   └── urls.py
│   │   │
│   │   └── payments/
│   │       ├── __init__.py
│   │       ├── models/
│   │       │   └── payment.py
│   │       │
│   │       ├── views/
│   │       │   └── payment.py
│   │       │
│   │       ├── serializers/
│   │       └── urls.py
│   │
│   ├── tests/
│   │   ├── api/
|   |   ├── models/
│   │   └── conftest.py
│   │
│   └── scripts/
│       ├── create_users.py
|       ├── dummy_products.py
│       ├── setup_auth.py
│       └── setup_db.py
│
├── frontend/
│   │
│   ├── package.json
│   ├── vite.config.js
│   │
│   ├── public/
│   │   ├── favicon.svg
│   │   └── icons.svg
│   │
│   └── src/
│       │
│       ├── main.jsx
│       ├── App.jsx
│       ├── App.css
│       │
│       ├── api/
│       │   └── api.js
│       │
│       ├── assets/
│       │   ├── hero.png
│       │   ├── react.svg
│       │   └── vite.svg
│       │
│       ├── pages/
│       │   ├── Login.jsx
│       │   ├── Page.jsx
│       │   ├── Student.jsx
│       │   ├── Staff.jsx
│       │   ├── Settings.jsx
│       │   ├── MFAOptions.jsx
│       │   ├── SetupTOTP.jsx
│       │   ├── VerifyMFA.jsx
│       │   ├── VerifySMS.jsx
│       │   ├── VerifyTOTP.jsx
│       │   └── ConfirmTOTP.jsx
│       │
│       ├── components/
│       │   ├── history.jsx
│       │   └── item.jsx
│       │   
│       │
│       ├── styles/
│       │   ├── Student.css
│       │   └── index.css
│       │
│       ├── utils/
│       │   └── csrf.js
│       │
│       └── 
│           
│
├── .gitignore
├── README.md
└── docker-compose.yml
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
python@3.11 -m venv venv
source venv/bin/activate
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

Note: After creating the virtual environments above, you need only do the following to go back in:

Mac:
```
cd backend
source venv/Bin/activate
```

Windows:
```
cd backend
```
Command Prompt:
```
.venv\Scripts\activate.bat
```
PowerShell:
```
.\.venv\Scripts\Activate.ps1
```

# Configure environment
cp .env.example .env   # edit DB / Redis credentials

For setting up the database run:
```
python scripts\setup_auth.py
python scripts\setup_db.py
python manage.py migrate
```
To setup the test users run:
```
python scripts\create_users.py
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
pytest tests
```
<h3>To run API or Model tests only</h3>
<h4>Model Tests</h4>

run
```
pytest tests/model
```

<h4>API Tests</h4>

run
```
pytest tests/api
```

<h4>Specific Model Tests</h4>

run
```
pytest tests/model/[file name]
```

<h4>Specific API Tests</h4>

run
```
pytest tests/api/[folder name i.e. orders]/[file name]
```


### Frontend

```bash
cd frontend
npm install
npm run dev          #http://localhost:5173/
```

---
<h3>Running test</h3>
Frontend testing uses Playwright <br>
To run tests:

run

```
cd frontend
npx playwright test
```


## User Roles


## Key API Endpoints

| Method | Endpoint                         | Description                    |
|--------|----------------------------------|--------------------------------|

| POST   | `/api/users/login/` |  User login endpoint <br>

| POST   | `/api/users/logout/` |  User logout endpoint <br>

| POST   | `/api/users/register/` | User registration endpoint <br>

| GET    | `/api/orders/view_history/` | User order history endpoint <br>

| GET    | `/api/orders/view_history/item/<int:id>/` | User order history items endpoint <br>

| GET    | `/api/orders/reorder/<int:id>/` | Reorder from order history endpoint <br>

| GET    | `api/orders/active-orders` | All of a user's active orders <br>

| GET    | `api/orders/active-orders/<int:order_id>/` | User's specific active order <br>

| GET    | `/api/products/all_products/`  | All products available endpoint <br>

| POST   | `api/payments/checkout/`  | Create checkout session endpoint <br>


