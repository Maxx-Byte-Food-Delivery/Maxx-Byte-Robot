import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './OrderTracker.css'; // Import CSS for styling
const ORDER_STATUS = {
  PLACED: 'placed',
  PREPARING: 'preparing',
  DISPATCHED: 'dispatched',
  DELIVERED: 'delivered',
};

const STATUS_CONFIG = {
  [ORDER_STATUS.PLACED]: {
    label: 'Order Placed',
    icon: '📦',
    color: '#4CAF50',
    description: 'Your order has been received',
  },

  [ORDER_STATUS.PREPARING]: {
    label: 'Preparing',
    icon: '⚙️',
    color: '#2196F3',
    description: 'We are preparing your order',
  },

  [ORDER_STATUS.DISPATCHED]: {
    label: 'Dispatched',
    icon: '🚚',
    color: '#FF9800',
    description: 'Your order is on the way',
  },

  [ORDER_STATUS.DELIVERED]: {
    label: 'Delivered',
    icon: '✅',
    color: '#8BC34A',
    description: 'Order delivered successfully',
  },
};

const OrderTracker = ({
  orderId = 'ORD-2024-001',
  initialStatus = ORDER_STATUSES.PLACED,
  id,
}) => {

  const [order, setOrder] = useState([]);
  const [currentStatus, setCurrentStatus] = useState(initialStatus);

  const [statusHistory, setStatusHistory] = useState([
    {
      status: ORDER_STATUS.PLACED,
      timestamp: new Date(),
    },
  ]);

  const [isAutoProgressing, setIsAutoProgressing] = useState(false);

  // FETCH ORDER
  const fetchOrder = async () => {

    try {

      const response = await axios.get(
        `http://127.0.0.1:8000/api/active-orders/${id}/`
      );

      setOrder(response.data);

    } catch (error) {

      console.error('Error fetching order:', error);
    }
  };

  useEffect(() => {
    fetchOrder();
  }, []);

  // AUTO STATUS UPDATE
  useEffect(() => {

    if (!isAutoProgressing) return;

    const statusSequence = [
      ORDER_STATUS.PLACED,
      ORDER_STATUS.PREPARING,
      ORDER_STATUS.DISPATCHED,
      ORDER_STATUS.DELIVERED,
    ];

    const currentIndex = statusSequence.indexOf(currentStatus);

    if (currentIndex < statusSequence.length - 1) {

      const timer = setTimeout(() => {

        const nextStatus = statusSequence[currentIndex + 1];

        setCurrentStatus(nextStatus);

        setStatusHistory((prev) => [
          ...prev,
          {
            status: nextStatus,
            timestamp: new Date(),
          },
        ]);

      }, 3000);

      return () => clearTimeout(timer);

    } else {

      setIsAutoProgressing(false);
    }

  }, [isAutoProgressing, currentStatus]);

  const handleManualStatusUpdate = (status) => {

    setCurrentStatus(status);

    setStatusHistory((prev) => [
      ...prev,
      {
        status,
        timestamp: new Date(),
      },
    ]);
  };

  return (

    <div className="order-tracker">

      <h1>Order Tracking</h1>

      <p>
        Order ID:
        {' '}
        <strong>{orderId}</strong>
      </p>

      <h2>
        Current Status:
        {' '}
        {STATUS_CONFIG[currentStatus].label}
      </h2>

      <div className="button-group">

        <button onClick={() =>
          handleManualStatusUpdate(ORDER_STATUS.PLACED)
        }>
          Placed
        </button>

        <button onClick={() =>
          handleManualStatusUpdate(ORDER_STATUS.PREPARING)
        }>
          Preparing
        </button>

        <button onClick={() =>
          handleManualStatusUpdate(ORDER_STATUS.DISPATCHED)
        }>
          Dispatched
        </button>

        <button onClick={() =>
          handleManualStatusUpdate(ORDER_STATUS.DELIVERED)
        }>
          Delivered
        </button>

      </div>

    </div>
  );
};

export default OrderTracker;