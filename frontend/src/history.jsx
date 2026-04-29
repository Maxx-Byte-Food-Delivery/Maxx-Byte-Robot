<!DOCTYPE html>
<html>
<body>

<h1>View Order History</h1>

<h2>Products</h2>

<ul>
  <form method="get" style="margin-bottom: 20px;">

  <!-- Search by item -->
  <input type="text" name="item" placeholder="Search by item name" value="{{request.GET.item}}">

  <!-- Filter by date -->
  <input type="date" name="date" value="{{request.GET.item}}">

  <button type="submit">Search</button>

</form>
  {% for order in orders %}
  <div style = "margin-top: 10px;">
    <strong>Date:</strong> {{ order.created_at|date:"M d, Y - H:i" }} </div>
    <li style="margin-bottom: 15px;">

      <a href="{% url 'item' order.id %}">
        View details
      </a>

      
      <form action="{% url 'reorder' %}" method="post" style="display:inline;">
        {% csrf_token %}
        <button type="submit">Reorder</button>
      </form>

      <div style="margin-left: 20px; margin-top: 5px;">
        {% for item in order.order_items.all %}
          <div>• {{ item.product.name }}</div>
        {% endfor %}
      </div>

    </li>
  {% endfor %}
</ul>

</body>
</html>