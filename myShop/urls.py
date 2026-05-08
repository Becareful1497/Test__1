from django.urls import path

from . import views


urlpatterns = [
    path('', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
]
