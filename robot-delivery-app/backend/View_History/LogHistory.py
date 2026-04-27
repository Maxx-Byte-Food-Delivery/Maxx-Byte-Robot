from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Order, Product, OrderItem

def View_History(request):

    # Get data
    orders = Order.objects.all()
    products = Product.objects.all()

    # Get query values
    item_query = request.GET.get('item')
    date_query = request.GET.get('date')

    # Filter by item name
    if item_query:
        orders = orders.filter(order_items__product__name__icontains=item_query)

    # Filter by date
    if date_query:
        orders = orders.filter(created_at__date=date_query)

    orders = orders.distinct()
    
    # Load template (you MUST choose ONE template here)
    template = loader.get_template('view_history/history.html')

    # Context contains BOTH datasets
    context = {
        'orders': orders,
        'products': products,
    }

    return HttpResponse(template.render(context, request))

def item(request, id):
    order = Order.objects.get(id=id)  # get the specific order


    template = loader.get_template('view_history/item.html')  # make sure path matches

    context = {
        'order': order,
    }

    return render(request, 'view_history/item.html', {'order': order})

def reorder(request, id):
    old_Order = Order.objects.get(id=id)

    new_Order = Order.objects.create(total_cost=old_Order.total_cost)



    for item in old_Order.order_items.all():
        OrderItem.objects.create(order = new_Order, product = item.product, quantity = item.quantity)

  

    return redirect('item', id = new_Order.id)