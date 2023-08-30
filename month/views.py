from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# # Create your views here.

months_dict = {
    "january":"Python Course",
    "february":"Java Course",
    "march":None,
    "april":"AWS Course",
    "may":"Data Science Course",
    "june":"Data Analytics Course",
    "july":"Software testing Course",
    "august":"Java Full Stack course",
    "september":"Python full stack Course",
    "october":"Mean+mern Course",
    "november":"Django Course",
    "december":"Flask Course",
}
# implementing html(unordered list,anchor tag)
def index(request):
    # list_month = ""
    month = list(months_dict.keys())
    # for i in month:
    #     capitalized_month = i.capitalize()
    #     month_path = reverse("month-name",args=[i])
    #     list_month += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_month}</ul>"
    # return HttpResponse(response_data)
    return render(request,"month/index.html",{"month_list":month})

# redirect path using reverse function (keyword argument)
def months_integer(request,months):
    month_int = list(months_dict.keys())
    if(months>len(month_int)):
        return HttpResponseNotFound("Invalid")
    
    redirect_months = month_int[months-1]
    redirect_path = reverse("month-name",args=[redirect_months])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/months/"+redirect_months)
    

def months_string(request,months):
    month_text = months_dict[months]
    # response_data = f"<h2>{month_text}</h2>"
    # return HttpResponse(response_data)
    return render(request,"month/month.html",{"monthname":months,"monthtext":month_text})
