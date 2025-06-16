# 3333333
from django.contrib import admin
from django.urls import path, include  # 33333333 include was added


urlpatterns = [
    path("admin/", admin.site.urls),
    
            # "challenges.urls" = "appname.file"
    # include("challenges.urls") is to load all the "urls" defined for the "challenges app"
    path("challenges/", include("challenges.urls"))
    # should handle request sent to challenges and forward internally(on the server) to "URLconf" of the "challenges" app
]


#"http://127.0.0.1:8000/challenge/January" to run
