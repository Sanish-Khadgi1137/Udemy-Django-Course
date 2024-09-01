# 3333333
"""
URL configuration for monthly_challenges project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
