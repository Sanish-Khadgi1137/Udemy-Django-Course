from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .form import ReviewForm
from .models import Review

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView




# def review(request):
#     if request.method == 'POST':
#         form1 = ReviewForm(request.POST)

#         if form1.is_valid():
#             form1.save()
            
#             return HttpResponseRedirect("thank-you")
        
#     else: 
#         form1 = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form2": form1
#     })
####################3333333333333333333333333333333333333333333333333


#using class View seeee https://docs.djangoproject.com/en/5.1/topics/class-based-views/
# class ReviewView(View):
#     #http method names "get"; django will automatically call  appropriate method name based on the kind of request that reached that View
#     def get(self, request):
#             form1 = ReviewForm()

#             return render(request, "reviews/review.html", {
#             "form2": form1
#             })
    
#     #http method name "post"
#     def post(self,request):
         
#         form1 = ReviewForm(request.POST)

#         if form1.is_valid():
#             form1.save()
           
#             return HttpResponseRedirect("thank-you")
        
#         #resending form with error message
#         return render(request, "reviews/review.html", {
#             "form2": form1
#             })
    ##############################3333333333333333333333333333333333333333333333333333333333


    #using FormView
# class ReviewView(FormView):
#     form_class = ReviewForm #the form_class property let django know which form class(from models.py) should be used  or rendering the form for providing the template and validating the input data
#     template_name = "reviews/review.html" #which template to use; automatically "form" is passed to a template file here review.html
#   #all the above get request is now handled by these 2 lines; validation also work with these line
    
#     #to redirect after success
#     success_url = "/thank-you"

#     #to save data to db; this method will be executed by django when a valid form is submitted
#     def form_valid(self, form):        #(form) is received as parameter after validation
#         form.save()
#         return super().form_valid(form) #"super().form_invalid(form)" for inheriting from parent class i.e "(FormView)" class which redirect us

####################333333333333333333333333333333333
#using CreateView which create form automaticall and save automatically; 
class ReviewView(CreateView):
    model = Review #to let know django which model it is about;we do not need "form" class we can directly get form based on model
    fields = "__all__"#or alternaqtively we can still use form class form, form.py which will be Modelform, we can not configure "label" and "error" messages here in CreateView but we can in form.py
    #form_class = ReviewForm #which form class to use
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    #above code is enought to render a form, validate a form, show error if needed and save data through the "Review" model if the data is submitted sucessfully

    

#############333333333333333333333333333333333333333
# def thank_you(request):
#     return render(request, "reviews/thank_you.html")

####################################333333333333333333333333333333333
# #classView of about thank_you funtion 
# class ThankYouView(View): #(View) is extended from above django.views; which is primarily deals with showing/displayin
#     #this post request have to post method
#     def get(self, request):
#             return render(request, "reviews/thank_you.html")

    ##########################3333333333333333333333333333333333333333333
#"TemplatesView" specificly focus allowing to build view classes that render template
class ThankYouView(TemplateView):
     template_name= 'reviews/thank_you.html'

     #to send dynamic data to template file
     def get_context_data(self, **kwargs):
         context=super().get_context_data(**kwargs)
         context["message1"] = "This works!"
         return context
     
##################333333333333333333333333333333333333333333
# class ReviewListView(TemplateView):
#     template_name="reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"]= reviews #"= reviews" is above variable and ["reviews"] is passed to html file
#         return context
    ###########################333333333333333333333333333333333333333333
#using "ListView" which is specifically for fetching a list of data based on some model
class ReviewListView(ListView):
    template_name="reviews/review_list.html"
    
    model=Review #"Review" is the class name of the model in models.py
 
    #overwriting default "object_list" to "reviews"
    context_object_name = "reviews"

    #to only render reviews greater than 4
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data


    
################################333333333333333333333333333333333333
# class SingleReviesView(TemplateView):
#     template_name="reviews/single_review.html"

#     def get_context_data(self, **kwargs): #thorugh this **kwargs we can get access dynamic segment eg "id" of individual reivew
#        context = super().get_context_data(**kwargs)
#        review_id = kwargs["id"] #"id" must be similar to the dynamic segment of id in urls.py i.e <int:id>
#        selected_review = Review.objects.get(pk=review_id)
#        context["reviews"]= selected_review
#        return context
    ###########################333333333333333333333333333333333333333333333
#using "DetialVeiw"

class SingleReviesView(DetailView):
    template_name="reviews/single_review.html"
    model = Review



