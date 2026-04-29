<!DOCTYPE html>
<html>
<head>
  <title>Order Details</title>
</head>

<body>


<h1><strong>Date:</strong> {{ order.created_at }}</h1>

<h2>Order Items:</h2>

<ul>
  {% for item in order.order_items.all %}
    <li>
      {{ item.product.name }} -
      Qty: {{ item.quantity }} -
      ${{ item.product.price }} × {{ item.quantity }} =
      ${{ item.subtotal|floatformat:2 }}
    </li>
  {% endfor %}
</ul>

<p><strong>Total:</strong> ${{ order.total_cost }}</p>

<p>
  <a href="{% url 'View_History' %}">Back to History</a>
</p>

</body>
</html>