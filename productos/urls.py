from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete


productos_patterns = ([
    path('', ProductList.as_view(), name="productos"),
    path('<int:pk>/<slug:slug>/', ProductDetail.as_view(), name='producto'),
    path('create/', ProductCreate.as_view(), name="create"),
    path('update/<int:pk>/', ProductUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', ProductDelete.as_view(), name="delete"),
], 'productos')
