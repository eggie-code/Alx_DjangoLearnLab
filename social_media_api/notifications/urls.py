from django.urls import path
from .views import NotificationListView, NotificationMarkReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification_list'),
    path('<int:pk>/mark_read/', NotificationMarkReadView.as_view(),
         name='notification_mark_read'),
]
