# 🤖 RoboEats – Robot Food Delivery Platform

A full-stack web application for managing autonomous robot food delivery.
Built with **Django REST Framework** (backend) and **React + Redux** (frontend).

---

## Architecture Overview

```
robot-delivery-app/
├── backend/                   Django + DRF + Django Channels
│   ├── config/                Settings, URLs, ASGI/WSGI
│   └── apps/
│       ├── accounts/          Custom user model, JWT auth, roles
│       ├── orders/            Menu items, order lifecycle
│       ├── robots/            Fleet models, telemetry, WS consumer
│       ├── mapping/           Zones, waypoints, geofencing
│       ├── navigation/        Route planning, Haversine distance
│       ├── power/             Charging stations & sessions
│       ├── transactions/      Secure payment records
│       └── delivery/          Robot assignment & completion logic
└── frontend/                  React 18 + Redux Toolkit
    └── src/
        ├── api/               Axios client + all service calls
        ├── store/slices/      auth / orders / robots Redux slices
        ├── hooks/             useAuth, useRobotSocket
        ├── components/        RobotStatusCard, OrderForm,
        │                      OrderTracker, MapView, ProtectedRoute
        └── pages/             LoginPage, OrderPage,
                               FleetDashboard, OrdersManagement, MapPage
```

---

## Quick Start (Docker)

```bash
# Clone and start everything
docker compose up --build

# Backend:  http://localhost:8000
# Frontend: http://localhost:3000
# Django Admin: http://localhost:8000/admin/
```

---

## Manual Setup

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env   # edit DB / Redis credentials

python manage.py migrate
python manage.py createsuperuser

# Run with Daphne (ASGI – supports WebSockets)
daphne -p 8000 config.asgi:application
```
<h3>Running test</h3>

```
cd backend
```
to run tests:<br>
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

| Role       | Access                                              |
|------------|-----------------------------------------------------|
| `customer` | Place orders, track delivery                        |
| `operator` | Fleet dashboard, map, assign robots, manage orders  |
| `admin`    | All of the above + Django admin                     |

---

## Key API Endpoints

| Method | Endpoint                         | Description                    |
|--------|----------------------------------|--------------------------------|
| POST   | `/api/v1/auth/token/`            | Obtain JWT tokens              |
| POST   | `/api/v1/auth/token/refresh/`    | Refresh access token           |
| POST   | `/api/v1/accounts/register/`     | Customer registration          |
| GET    | `/api/v1/accounts/me/`           | Current user profile           |
| GET    | `/api/v1/orders/menu/`           | Available menu items           |
| POST   | `/api/v1/orders/`                | Place a new order              |
| POST   | `/api/v1/orders/{id}/cancel/`    | Cancel an order                |
| GET    | `/api/v1/robots/`                | List all robots (operator+)    |
| POST   | `/api/v1/robots/{id}/command/`   | Send robot command             |
| GET    | `/api/v1/robots/{id}/telemetry/` | Last 50 telemetry records      |
| GET    | `/api/v1/mapping/zones/`         | Delivery zones                 |
| GET    | `/api/v1/mapping/waypoints/`     | Waypoints (charging, pickup…)  |
| POST   | `/api/v1/navigation/routes/plan/`| Estimate route distance/ETA    |
| GET    | `/api/v1/power/stations/`        | Charging stations              |
| POST   | `/api/v1/transactions/initiate/` | Initiate payment               |
| POST   | `/api/v1/delivery/{id}/assign/`  | Assign nearest robot to order  |
| POST   | `/api/v1/delivery/{id}/complete/`| Mark delivery complete         |

### WebSocket

```
ws://localhost:8000/ws/robots/{robot_id}/
```
Connect to receive real-time telemetry for a robot. Also accepts telemetry
pushes from robot hardware clients.

---

## Tech Stack

| Layer       | Technology                                          |
|-------------|-----------------------------------------------------|
| Backend     | Django 4.2, Django REST Framework, Django Channels  |
| Auth        | JWT via `djangorestframework-simplejwt`             |
| Database    | PostgreSQL 16                                       |
| Cache / WS  | Redis 7 + channels-redis                           |
| Frontend    | React 18, Redux Toolkit, React Router 6            |
| HTTP Client | Axios (with auto-refresh interceptor)               |
| Maps        | Leaflet + react-leaflet (OpenStreetMap – no API key)|
| Containers  | Docker Compose                                      |

---

## Next Steps

- [ ] Integrate a real routing engine (OSRM / GraphHopper)
- [ ] Add Stripe / PayPal payment gateway in `transactions/views.py`
- [ ] Connect robot hardware via MQTT (Eclipse Mosquitto) or robot REST API
- [ ] Add push notifications (Firebase / WebPush) for order status changes
- [ ] Implement geofencing enforcement in `mapping/`
- [ ] Add end-to-end tests (pytest-django + React Testing Library)
- [ ] Production deployment: nginx → Daphne, Certbot TLS
