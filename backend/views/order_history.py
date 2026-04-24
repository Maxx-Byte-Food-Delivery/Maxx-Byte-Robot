from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.models.order import Order


@api_view(['GET', 'POST'])

@login_required
def order_history(request):
    # Filter orders for the logged-in user [3]
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'order_history.html', context)
        
    
    