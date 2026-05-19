import React, { useState, useEffect } from 'react';
import API from "../api/api";

const ActiveOrders = () => {

    const [orders, setOrders] = useState([]);

    useEffect(() => {
        fetchOrders();
    }, []);

    // FETCH ACTIVE ORDERS
    const fetchOrders = async () => {

        try {

            const response = await API.get('/orders/active-orders/') 

            setOrders(response.data);

        } catch (error) {

            console.error("Error fetching orders:", error);
        }
    };

    // UPDATE ORDER STATUS
    const updateStatus = async (id, newStatus) => {

        try {

            await API.patch(
                `http://127.0.0.1:8000/api/orders/active-orders/${id}/`,
                {
                    status: newStatus
                }
            );

            // REFRESH ORDERS
            fetchOrders();

        } catch (error) {

            console.error("Error updating status:", error);
        }
    };

    return (

        <div className="order-container">

            <h1>Active Food Orders</h1>

            {orders.map(order => (

                <div
                    key={order.id}
                    className="order-card"
                    style={{
                        border: '1px solid #ccc',
                        margin: '10px',
                        padding: '10px',
                        borderRadius: '10px'
                    }}
                >

                    <h3>
                        Order #{order.id} - {order.customer_name}
                    </h3>

                    <p>
                        <strong>Items:</strong>
                        {" "}
                        {order.items}
                    </p>

                    <p>
                        <strong>Status:</strong>
                        {" "}
                        {order.status}
                    </p>

                    <button
                        onClick={() =>
                            updateStatus(order.id, 'Preparing')
                        }
                    >
                        Preparing
                    </button>

                    <button
                        onClick={() =>
                            updateStatus(order.id, 'Out for Delivery')
                        }
                        style={{ marginLeft: '10px' }}
                    >
                        Out for Delivery
                    </button>

                    <button
                        onClick={() =>
                            updateStatus(order.id, 'Delivered')
                        }
                        style={{ marginLeft: '10px' }}
                    >
                        Mark Delivered
                    </button>

                </div>
            ))}

        </div>
    );
};

export default ActiveOrders;