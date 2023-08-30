from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def may(request):
#     return HttpResponse("summer season.")

season_dict = {
    "Summer Season":"February-March-April-May",
    "Rainy Season":"June-July-August-September",
    "Winter Season":"October-November-December-January"
}

# implementing html(unordered list,anchor tag)
def index(request):
    # list_season = ""
    season = list(season_dict.keys())
    # for i in season:
    #     season_path = reverse("season-name",args=[i])
    #     list_season += f"<li><a href = \"{season_path}\">{i}</a></li>"
    # respose_data = f"<ul>{list_season}</ul>"
    # return HttpResponse(respose_data)
    return render(request,"season/index.html",{"season_list":season})


# redirect path using reverse function(keyword argument)
def season_details_integer(request,seasons):
    season_int = list(season_dict.keys())
    if(seasons>len(season_int)):
        return HttpResponseNotFound("Invalid - Enter 1/2/3 to know season months")
    redirect_season = season_int[seasons-1]
    redirect_path = reverse("season-name",args=[redirect_season])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/seasons/"+redirect_season)

# def season_details_string(request,month):
#     if month in ("february","march","april","may"):
#         season = "Summer Season."
#     elif month in ("june","july","august","september"):
#         season = "Rainy Season."
#     elif month in ("october","november","december","january"):
#         season = "Winter Season."
#     else:
#         return HttpResponseNotFound("Please put valid month...")
    
#     return HttpResponse(season)

def season_details_string(request,seasons):
    try:
        season_text = season_dict[seasons]
        # response_data = f"<h2>{season_text}</h2>"
        response_data = render_to_string("season/season.html",
            {"seasonname":seasons,"seasonmonths":season_text})
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Invalid seasons entered.")





