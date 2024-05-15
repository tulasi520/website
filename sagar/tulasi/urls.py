from django.urls import path
from. import views


urlpatterns = [
    path('',views.index,name='index'),
    path('tulasi/add_expenses',views.add_expenses, name='add_expenses'),
    
]
