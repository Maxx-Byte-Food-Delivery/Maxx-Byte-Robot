from django.urls import path
from . import LogHistory

urlpatterns = [
    # Add 'View_History/' to the path string
    path('View_History/', LogHistory.View_History, name='View_History'),
    path('View_History/item/<int:id>/', LogHistory.item, name='item'),
    path('reorder/', LogHistory.reorder, name='reorder'),
]