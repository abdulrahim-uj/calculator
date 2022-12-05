from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcop, name="calculator"),
    path('calc/', views.calcresult, name="calc-result"),
]
