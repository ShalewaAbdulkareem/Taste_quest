from django.urls import path
from fruits_app import views




app_name = 'fruits_app'

urlpatterns = [
    # path('index1/', views.index1, name='index1'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('single-product/<int:id>/', views.single_product, name='single-product'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/<int:id>/', views.single_blog, name='single-blog'),
]