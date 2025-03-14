from django.urls import path
from . import views

urlpatterns = [
    path('', views.stack, name='stack'),
    # path('take_product/<slug:product_slug>/', views.take_product, name='take_product')
    path('take_product/<int:product_id>/', views.take_product, name='take_product'),
    path('take_product/<int:product_id>/<int:taken_item_id>/+', views.take_another, name='take_another'),
    path('put_back/<int:product_id>/<int:taken_item_id>/', views.put_back, name='put_back'),  # put back just one
    path('put_all/<int:product_id>/<int:taken_item_id>/', views.put_all, name='put_all'),  # put all items back
    path('order/', views.order, name='order'),
]
