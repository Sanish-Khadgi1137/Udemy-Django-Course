from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#from .form import ReviewForm
from .models import Review

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView


class ReviewView(CreateView):
    model = Review
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message1"] = "This works!"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"

    model = Review

    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data


class SingleReviewsView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    #for getting data from session
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    #this get_context.. content "SingleReviees" which is fetched automatically, so storing already generated context in a "context" variable

        
        loaded_review = self.object #this especial "object" property in this class give access to that automated review 
        request = self.request #to access request; see official docs

        # #trying to access any session data can fail if it was not set before; if we load the site without out any session set ie. if we visit for first time we would be greated by "KeyError"
        # favorite_id = request.session["favorite_review"] # because in this line we tries to get the favorite out of the session eventhough this key does not exist
        
        #solution/safer way if not sure it has been set before use the get method
        favorite_id = request.session.get("favorite_review")

        #check if the review id stored in the session in the "favorite_review"(see @123 below) key = to the review_id for which i loaded review here; to achive this we need to get access to request and to that object in this detail view; see above###
        context["is_favorite"]= favorite_id == str(loaded_review.id) #checking if id match the favroite review; adding more data to above "context", using str() to change the sring. see @445 below
        return context



#for session
class AddFavoriteView(View):
    def post(self, request): #this method trigger for incoming post request
        review_id = request.POST["review_id"] #getting review id of the post
        
        #we were storeing object in session which was wrong
        # fav_review = Review.objects.get(pk=review_id) #to get 'full review' based on 'review_id' 

        #storing "fav_review" in session key "["favorite-review"]"
        # request.session["favorite_review"] = fav_review #under the hood django make sure that this data is stored to the data base along all other session data that belongs to me and this data is always be accessible if I send request this server and for every user different session with different piece of data is kept around; so multiple users can have differnet favorites
        
        #we got this error "TypeError at /reviews/favorite Object of type Review is not JSON serializable" error 500 becuase we were storing review object in our session not distionary/list/string/integer/boolean; under the hood django just take whatever store in the session and serialized to a format called json(javascript object notation) a popular data format in web development
        #the problem is objects can not be serialized because those contains "methods" also and those cannot be translated to json, so only primitive values can be stored in the session
        request.session["favorite_review"] = review_id #@123 we just stored "id", now it wroks; we receive 'review_id' from the form submission, even it is actually number and such data is always treated as string eg "1". see @445 above

        return HttpResponseRedirect("/reviews/" + review_id) # ..reviews/3(favorite)
    
    #http://127.0.0.1:8000/reviews/3 see from 3 becuase we deleted 2 datas before in db