from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HelloOrderView.as_view(), name='order_view'),
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name='update_order_status'),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name='user_order_status'),
    path('user/<int:user_id>/orders/<int:order_id>', views.UserOrderDetailView.as_view(), name='user_order_detail'),
]
