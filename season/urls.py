from django.urls import path
from . import views

urlpatterns = [
    # path("may",views.may)
    path("",views.index,name='index_season'),
    path("<int:seasons>",views.season_details_integer),
    path("<str:seasons>",views.season_details_string,name="season-name")
]