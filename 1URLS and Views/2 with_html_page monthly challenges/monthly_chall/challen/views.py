from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

monthly_challenges_dic={
    "january" : "Do not eat mean for entire months",
    "february" : "Walk at least for 20 minute everyday",
    "march" : "Practise django for 30 miutes everyday ",
    "april" : "a",
    "may" : "m",
    "june" : "JU",
    "july" : 'Jul',
    "august" : "Aug",
    "september" : "S",
    "october" : "bd",
    "november" : 'N',
    "december" : "D"

}

def index(request):
    #hard-coded style; triple quotes """ """ for multi line string
    # resp_data = """
    #     <ul>
    #         <li>
    #         <a href = "/challen/january">January</a>
    #         </br>
    #         <a href = "/challen/february">February</a>
    #         </li>
    #     </ul>   
    # """
    # return HttpResponse(resp_data)

    #dynamic style

    months = list(monthly_challenges_dic.keys())

    list_item = ""

    for month in months:

        capitalized_month= month.capitalize()
        
        month_path = reverse("chal_mont", args=[month])#month is small letter month from list; argument is passes for place holder in url.py here "<month2>"

        list_item += f"<li><a href= \"{month_path}\">{capitalized_month}</a></li>"#we used double quots "" twice so to scape it we used \ \
#this html code is not well structure and lack key element for optimization for search engine 
    resp_data = f"<ul>{list_item}</ul>"

    return HttpResponse(resp_data)


def chal(request, month2):
    try:
        chal_text = monthly_challenges_dic[month2]
        response_data = f"<h1>{chal_text}</h1>"
        return HttpResponse(response_data)

    except:
         return HttpResponseNotFound("<h1>This month is not supported!<h1>")

