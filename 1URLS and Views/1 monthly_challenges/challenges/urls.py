from django.urls import path
from . import views  # "." means from same folder where we are at now

# when request reaches this url a veiw function get triggred
'''static way
urlpatterns = [
    path("january", views.january),  # actually challeges/january
    # if request reaches "january" execute "views.january"
    # this creates urlconfig or URLconf defined in our "challenges" app which is part of "monthly_challenges" project need to connect 'challenges' app to entire project, we need to make entire project's URLconf aware of URLconf of this specific app to do so go to "urls" file of the "monthly_challenges" folder

    path("february", views.february)
    
    ]
'''

#dynamic way
urlpatterns = [
    #path("<str:month1>", views.monthly_challenges1) #str: for string type in url eg. "challenges/january"
    #path("<month1>", views.monthly_challenges1),#"<month1>" is a place holder for "views"(here month's htmls)

    path("<int:month1>", views.monthly_challenges_by_num), #int: for search with integer type in url eg. "challenges/1"

    #path("<month1>", views.monthly_chall_dic)

    #professionaly; more dynamic; no hard-coded
    path("<month1>", views.monthly_chall_dic, name= "mon-chal")#we use this "name" in reverse function


]

# to run go to port 8000/challenges/january