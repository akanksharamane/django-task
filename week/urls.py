from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index_week"),
    path("<int:weeks>",views.weeks_integer,name = "week-name"),
    path("<str:weeks>",views.weeks_string,name="week-name")
]