from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import ReviewForm

from .models import Review



# def review(request):
#     if request.method == 'POST':
#         entered_username = request.POST["username5"] #extracting data manually

#         #manual validation and there are lots of problem in manual validation like different error msges for each error; solution is using built in django form support/feature method form.py
#         if entered_username == "": #and len(entered_username) >= 10:
           
#             return render(request, "reviews/review.html", {
#                 "has_error": True
#             })

#         print(entered_username)
#         return HttpResponseRedirect("thank-you")


#     return render(request, "reviews/review.html", {
#                 "has_error": False
#             })#this is for GET method/initial page/page to input


#using form method
def review(request):
    
    #we can put form=form instead of form1 and form2
    if request.method == 'POST':

        # #to update existing data
        # existing_data = review.objects.get(pk=1)
        # form1 = ReviewForm(request.POST, instance= existing_data )

        form1 = ReviewForm(request.POST)# "POST" of "request.POST" here is collected data 

        #this catch even form built-in validation is bypassed i.e required is deleted from developer mode; to check for empty submit and .... but emplty submission is automatically block by built-in form  using reqeired keyword see inspection-Element
        if form1.is_valid():#is_valid is built-in function in Form
            #print(form1.cleaned_data) #cleaned-data is built-in variable contain collected data; we get dictionary in console
           
           #saving data instead of displayin; "user_name"= is from models.py and ['user_name'] from form.py
            
            # review= Review(user_name=form1.cleaned_data['user_name'],
            #                    review_text=form1.cleaned_data['review_text'], 
            #                    rating=form1.cleaned_data['rating'])
            # review.save()
            
            #we do not need to instanciate the form in Model form li above 4 lines
            form1.save()
            
            return HttpResponseRedirect("thank-you")

    #for GEt method or brand new form
    #using forms forms.py
    else: #just using else we can get error message, but other field which were valid get save and show them in new form/ if it not go to validation will not print error message
        form1 = ReviewForm()

    return render(request, "reviews/review.html", {
        "form2": form1
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
