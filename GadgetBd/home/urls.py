from django.urls import path
from. import views

app_name='homeApp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('product-detail/<str:id>', views.prodDetail, name='prodDetail'),
]