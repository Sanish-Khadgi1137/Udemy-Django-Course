#convention is to create templates folder insider app and folder with app's name inside templetes
#"filter": in views.py only core business logic are done professionally; we can do less important logic(built in function) can be done in html file to using DTL; which is called "filter"
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string



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
    "december" : None

}

def index(request):
    """Displaying list of month"""

    months = list(monthly_challenges_dic.keys())

    # list_item = ""

    # for month in months:

    #     capitalized_month= month.capitalize()
        
    #     month_path = reverse("chal_mont", args=[month])#month is small letter month from list

    #     list_item += f"<li><a href= \"{month_path}\">{capitalized_month}</a></li>"


    # resp_data = f"<ul>{list_item}</ul>"

    # return HttpResponse(resp_data)

#tags : doing above logic using tags in index.html
    return render(request, "chalapp/index2.html", {
         "mons" : months
    })


def chal(request, month2):
    """Displaying clicked of the month"""
    try:
        chal_text = monthly_challenges_dic[month2]
                                         #app-name/file  app-name to avoid clashing of files with same name of different apps
        # response_data = render_to_string("chalapp/challenges.html")#we need to configure/inform template folder or app to setting.py of project in "DIRS: []" or for app "INSTALLED_APPS = [

        # return HttpResponse(response_data)
     
        #shorcuts; instead above 2 lines
        # return render(request, "chalapp/challenges.html")#request is necessary for render()
      
        #dynamic; for dynamic we use html + special DTL(django templated language) syntax eg "{{}}" in html file; commented {{}} is not allowed in normal-html file
        return render(request, "chalapp/challenges2.html", {
            "text": chal_text,
            'month_name' : month2.capitalize()#do this inside html file using DTL for doing simple operation in html file

            })#we see hard coded text not place holder in html inspect because django analize and replaces those {{}} on the server and generate final html string or file and send to browser so browser only received that finish html hard coded string

    except:
        #return HttpResponseNotFound("<h1>This month is not supported!<h1>")

        #404 error with 404.html file
        response_data=render_to_string("404.html") #since 404.html file is in root template folder and have added to template DIR
        return HttpResponseNotFound(response_data)

        # raise Http404()#we can pass error message from here or it automatically find 404.html file in the root template file and has to be named 404.html
        # #we still get error because fo DEBUG True in setting.py we need to make it False
