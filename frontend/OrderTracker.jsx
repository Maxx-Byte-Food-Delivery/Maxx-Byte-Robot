import React, { useState, useEffect } from 'react';
import './OrderTracker.css';

const ORDER_STATUSES = {
  PLACED: 'placed',
  PREPARING: 'preparing',
  DISPATCHED: 'dispatched',
  DELIVERED: 'delivered',
};

const STATUS_CONFIG = {
  [ORDER_STATUSES.PLACED]: {
    label: 'Order Placed',
    icon: '📦',
    color: '#4CAF50',
    description: 'Your order has been received',
  },
  [ORDER_STATUSES.PREPARING]: {
    label: 'Preparing',
    icon: '⚙️',
    color: '#2196F3',
    description: 'We are preparing your order',
  },
  [ORDER_STATUSES.DISPATCHED]: {
    label: 'Dispatched',
    icon: '🚚',
    color: '#FF9800',
    description: 'Your order is on the way',
  },
  [ORDER_STATUSES.DELIVERED]: {
    label: 'Delivered',
    icon: '✅',
    color: '#8BC34A',
    description: 'Order delivered successfully',
  },
};

const OrderTracker = ({ orderId = 'ORD-2024-001', initialStatus = ORDER_STATUSES.PLACED }) => {
  const [currentStatus, setCurrentStatus] = useState(initialStatus);
  const [statusHistory, setStatusHistory] = useState([
    {
      status: ORDER_STATUSES.PLACED,
      timestamp: new Date(Date.now() - 3600000),
    },
  ]);
  const [isAutoProgressing, setIsAutoProgressing] = useState(false);

  // Real-time status update simulation
  useEffect(() => {
    if (!isAutoProgressing) return;

    const statusSequence = [
      ORDER_STATUSES.PLACED,
      ORDER_STATUSES.PREPARING,
      ORDER_STATUSES.DISPATCHED,
      ORDER_STATUSES.DELIVERED,
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

  const formatTime = (date) => {
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    if (diffDays < 7) return `${diffDays}d ago`;

    return date.toLocaleDateString();
  };

  const getStatusIndex = (status) => {
    const sequence = [
      ORDER_STATUSES.PLACED,
      ORDER_STATUSES.PREPARING,
      ORDER_STATUSES.DISPATCHED,
      ORDER_STATUSES.DELIVERED,
    ];
    return sequence.indexOf(status);
  };

  const currentStatusIndex = getStatusIndex(currentStatus);

  return (
    <div className="order-tracker">
      <div className="tracker-header">
        <h1>Order Tracking</h1>
        <p className="order-id">Order ID: <strong>{orderId}</strong></p>
      </div>

      {/* Status Timeline */}
      <div className="status-timeline">
        {Object.values(ORDER_STATUSES).map((status, index) => {
          const isCompleted = index <= currentStatusIndex;
          const isCurrent = status === currentStatus;
          const config = STATUS_CONFIG[status];

          return (
            <div
              key={status}
              className={`timeline-item ${isCompleted ? 'completed' : ''} ${
                isCurrent ? 'current' : ''
              }`}
            >
              <div
                className="timeline-dot"
                style={{
                  backgroundColor: isCompleted ? config.color : '#ddd',
                  borderColor: isCurrent ? config.color : 'transparent',
                }}
              >
                <span className="status-icon">{config.icon}</span>
              </div>
              <div className="timeline-content">
                <h3>{config.label}</h3>
                <p className="status-description">{config.description}</p>
                {statusHistory.find((h) => h.status === status) && (
                  <p className="status-time">
                    {formatTime(
                      statusHistory.find((h) => h.status === status).timestamp
                    )}
                  </p>
                )}
              </div>
              {index < Object.values(ORDER_STATUSES).length - 1 && (
                <div
                  className={`timeline-connector ${
                    index < currentStatusIndex ? 'completed' : ''
                  }`}
                  style={{
                    backgroundColor: index < currentStatusIndex ? '#4CAF50' : '#ddd',
                  }}
                />
              )}
            </div>
          );
        })}
      </div>

      {/* Status Update History */}
      <div className="status-history">
        <h2>Update History</h2>
        <div className="history-list">
          {statusHistory.map((entry, index) => (
            <div key={index} className="history-item">
              <span className="history-status">
                {STATUS_CONFIG[entry.status].label}
              </span>
              <span className="history-time">
                {entry.timestamp.toLocaleString()}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Manual Status Controls (for testing) */}
      <div className="controls">
        <h3>Quick Actions</h3>
        <div className="button-group">
          <button
            className="btn btn-primary"
            onClick={() => setIsAutoProgressing(!isAutoProgressing)}
          >
            {isAutoProgressing ? 'Stop Auto-Update' : 'Start Auto-Update'}
          </button>
          <button
            className="btn btn-secondary"
            onClick={() => handleManualStatusUpdate(ORDER_STATUSES.PLACED)}
          >
            Placed
          </button>
          <button
            className="btn btn-secondary"
            onClick={() => handleManualStatusUpdate(ORDER_STATUSES.PREPARING)}
          >
            Preparing
          </button>
          <button
            className="btn btn-secondary"
            onClick={() => handleManualStatusUpdate(ORDER_STATUSES.DISPATCHED)}
          >
            Dispatched
          </button>
          <button
            className="btn btn-secondary"
            onClick={() => handleManualStatusUpdate(ORDER_STATUSES.DELIVERED)}
          >
            Delivered
          </button>
        </div>
      </div>
    </div>
  );
};

export default OrderTracker;
