from django.urls import path
from . import views

urlpatterns = [
    # path("", views.review),

    #using classview/FormView here "ReviewView" is a  class name and .as_view() is a built-in method, we get it from extending "View"; which make sure django is able to find those get() and post()
    path("", views.ReviewView.as_view()),


    # path("thank-you", views.thank_you)

    #form class view
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),

    # path("reviews/<int:id>", views.SingleReviesView.as_view())

    #for DetailVeiw "pk" is used to identify specific review
    path("reviews/<int:pk>", views.SingleReviesView.as_view())
]