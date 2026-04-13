// src/api/index.js – All API service calls in one place

import client from "./client";

// ── Auth ──────────────────────────────────────────────────────────────────
export const authApi = {
  login:   (credentials) => client.post("/auth/token/", credentials),
  refresh: (token)       => client.post("/auth/token/refresh/", { refresh: token }),
  me:      ()            => client.get("/accounts/me/"),
  register:(data)        => client.post("/accounts/register/", data),
};

// ── Orders ────────────────────────────────────────────────────────────────
export const ordersApi = {
  list:       (params)   => client.get("/orders/", { params }),
  get:        (id)       => client.get(`/orders/${id}/`),
  create:     (data)     => client.post("/orders/", data),
  cancel:     (id)       => client.post(`/orders/${id}/cancel/`),
  menuItems:  (params)   => client.get("/orders/menu/", { params }),
};

// ── Robots ────────────────────────────────────────────────────────────────
export const robotsApi = {
  list:       (params)   => client.get("/robots/", { params }),
  get:        (id)       => client.get(`/robots/${id}/`),
  update:     (id, data) => client.patch(`/robots/${id}/`, data),
  telemetry:  (id)       => client.get(`/robots/${id}/telemetry/`),
  command:    (id, cmd)  => client.post(`/robots/${id}/command/`, cmd),
};

// ── Mapping ───────────────────────────────────────────────────────────────
export const mappingApi = {
  zones:      ()         => client.get("/mapping/zones/"),
  waypoints:  (params)   => client.get("/mapping/waypoints/", { params }),
  createWaypoint: (data) => client.post("/mapping/waypoints/", data),
};

// ── Navigation ────────────────────────────────────────────────────────────
export const navigationApi = {
  routes:     (params)   => client.get("/navigation/routes/", { params }),
  planRoute:  (data)     => client.post("/navigation/routes/plan/", data),
};

// ── Power ─────────────────────────────────────────────────────────────────
export const powerApi = {
  stations:   ()         => client.get("/power/stations/"),
  sessions:   (params)   => client.get("/power/sessions/", { params }),
};

// ── Transactions ──────────────────────────────────────────────────────────
export const transactionsApi = {
  list:       (params)   => client.get("/transactions/", { params }),
  get:        (id)       => client.get(`/transactions/${id}/`),
  initiate:   (data)     => client.post("/transactions/initiate/", data),
};

// ── Delivery ──────────────────────────────────────────────────────────────
export const deliveryApi = {
  assign:     (orderId)  => client.post(`/delivery/${orderId}/assign/`),
  complete:   (orderId)  => client.post(`/delivery/${orderId}/complete/`),
};

// ── WebSocket helper ──────────────────────────────────────────────────────
export function connectRobotSocket(robotId, onMessage) {
  const base = (process.env.REACT_APP_WS_URL || "ws://localhost:8000").replace(/\/$/, "");
  const ws   = new WebSocket(`${base}/ws/robots/${robotId}/`);
  ws.onmessage = (e) => onMessage(JSON.parse(e.data));
  return ws;
}
