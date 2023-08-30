from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.
# def index(request):
#     return HttpResponse("This works")

weeks_of_month = {
    "Monday":"First day of the week.",
    "Tuesday":"Second day of the week.",
    "Wednesday":"Third day of the week.",
    "Thursday":"Fourth day of the week.",
    "Friday":"Fifth day of the week.",
    "Saturday":"Sixth day of the week.",
    "Sunday":"Seventh day of the week.",
}

# using html tags.(unordered list, anchor tag)
def index(request):
    # list_weeks = ""
    weeks = list(weeks_of_month.keys())
    # for i in weeks:
    #     capitalized_week = i.capitalize()
    #     week_path = reverse("week-name",args=[i])
    #     list_weeks += f"<li><a href = \"{week_path}\">{capitalized_week}</a></li>"
    # response_data = f"<ul>{list_weeks}</ul>"
    # return HttpResponse(response_data)
    return render(request,"week/index.html",{"weekdays_list":weeks})


# redirect path using reverse function.
def weeks_integer(request,weeks):
    weeks_int = list(weeks_of_month.keys())
    if(weeks>len(weeks_int)):
        return HttpResponseNotFound("Invalid week day.")
    
    redirect_week = weeks_int[weeks-1]
    redirect_path = reverse("week-name",args=[redirect_week])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/weeks/"+redirect_week)

def weeks_string(request,weeks):
    try:
        week_text = weeks_of_month[weeks]
        # response_data = f"<h2>{week_text}</h2>"
        return render(request,"week/week.html",{"weektext":week_text,"week_days":weeks})
        # response_data = render_to_string("week/week.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Invalid week.")

