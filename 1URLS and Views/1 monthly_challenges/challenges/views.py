
"""in the cycle of user visiting our site/server, exchange request and resposed 
"view.py" is responsible for process the request of client/browser (may be reach out to db)
 and repsonse the request"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse #33333


# this function is executed by django not by us when an incomming request hit this django server and forwarded to this function; for this argument "request" is-
#  -passed to the function eg. def index(request) 

'''static way
#def index(request): #for general we use index

def january(request):

  # 333333333333all down from here
    # this object"HttpResponse" return response to client/browser
    return HttpResponse("Do not eat mean for entire months")
    # this file displaying "This works!" to browser

def february(request):
    return HttpResponse("Walk at least for 20 minute ev`eryday")
'''


# #dynamic way
# def monthly_challenges1(request, month1):
#     challenge_text = None;#setting default value for our variable "challenge_text"

#     if month1 == "january":
#         challenge_text = "Do not eat mean for entire months"
#     elif month1 == "february": 
#         challenge_text = "Walk at least for 20 minute everyday"
#     elif month1 == "March":
#         challenge_text == "Practise django for 30 miutes everyday "
#     else:
#         return HttpResponseNotFound("This month is not supported") #to send 4O4(four O four error not four zero four)
    

#     return HttpResponse(challenge_text)

# """django won't know when to call this function so we need urls.py files inside same folder as views.py"""

#more dynamic
monthly_challenges_dic={
    "January" : "Do not eat mean for entire months",
    "February" : "Walk at least for 20 minute everyday",
    "March" : "Practise django for 30 miutes everyday ",
    "April" : "a",
    "May" : "m",
    "June" : "JU",
    "July" : 'Jul',
    "August" : "Aug",
    "September" : "S",
    "October" : "bd",
    "November" : 'N',
    "December" : "D",
    "Dulimber" : "cartonist"

}
#since "key" are in capital letter in dictionary so we need to type url in pascal case eg no "january", need to type "January"

def monthly_chall_dic(request, month1):
    try:
        challenges_text = monthly_challenges_dic[month1]#used key to get text
        response_data = f"<h1>{challenges_text}<h1>"#for html page
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!<h1>")# <h1> added to make it html page
    #return HttpResponse(challenges_text)

#any response with 300 is redirect

#from this we can type interger instead of name
#if we type interger browser redirect(302) response to  challenges/month
def monthly_challenges_by_num(request, month1):
    months= list(monthly_challenges_dic.keys()) #.keys() give all the "keys" in a list in order manner eg. January is first and February is second
                  #list[] make it real list before .key() give object in []; so we can access item with index
    
    if month1 > len(months):
        return HttpResponseNotFound("Invalid month")#to counter index error

    #this line is responsible to give month from interger to string, by pointing month from list
    redirect_month = months[month1-1]#"month1" = index(number) and "months" = list[]
                      #month1 - 1 since list start from 0

                                #/challenges/ is hard-coded
    #return HttpResponseRedirect("/challenges/" + redirect_month)#is redirect to old link 
                               #link "/challenges/" must be exactly same as in urls.py/challenges

    #professional way; no hard-coded

    #this makes no error even url changes in urls.py; e.g /challenges/ to /challenge/
    redirect_path = reverse("mon-chal", args=[redirect_month])#"mon_chal" from urls.py\challenges
    #this build the path look like /challenges/
    #args=[] is argument passed here "month" which comes "/challenges/month" eg /challenge

    return HttpResponseRedirect(redirect_path)

#if we need to add more months we do not need to make any changes to function we just need to add it in dictionary