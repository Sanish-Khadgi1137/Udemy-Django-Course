from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),

   #this url must be before primary key <int:pk> because we do not want 'favorite" to be interpretated as primary key
    path("reviews/favorite", views.AddFavoriteView.as_view()),

    path("reviews/<int:pk>", views.SingleReviewsView.as_view())
]

#if we do not want to store user specific data for forever/ do not want to manage with models or we want them to store in data base temporarly; for such kind of data we use sessions eg stay log in even we refersh the browser
#session is a "ongoing connetion(that presist and live on even if the browser is closed/the computer is shutdown)" between a client(browser) and server 
#session is a long term relation between browser and the server; it can be cleared, deleted and reset, develper decide how long it will live
#eg user authentication access
#server store session data and session identifier - stored in session storage typically in db
#client(browser) stores a cookie with "Session ID" which is sent by the server; which makes client enable in future to sent that cookie to server and server can look up that session in db and sends that session specific data to client or do what is need to be done  with the session data 
#if the "session data" for example contents the information that "this client is logged in already" then the server may grant access protected resources
#django already create the cookie, send that cookie to the cline(browser), store the session in db, we as a developer just need to configure how the session should behave eg how long a session should be active and then we can write to and read from session data as needed
# we make changes in setting.py