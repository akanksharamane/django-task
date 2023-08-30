from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index_month"),
    path("<int:months>",views.months_integer),
    path("<str:months>",views.months_string,name="month-name")
]