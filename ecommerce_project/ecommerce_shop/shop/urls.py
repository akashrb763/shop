
from django.urls import path

from . import views
app_name='shop'

urlpatterns=[
    path('',views.allprodCat,name='allprodCat'),
    path('<slug:c_slug>/',views.allprodCat,name='prod_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodDetail, name='product_catdatails'),

]

