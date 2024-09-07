from django.shortcuts import render, HttpResponseRedirect
from django.views import View

from .forms import ProfileForm
from .models import UserProfile

from django.views.generic.edit import CreateView
from django.views.generic import ListView

# #manually storing files
# def store_file(file): #the "temp" folder can be anywhere in the project
#     with open("temp/image.jpg", "wb+") as dest:# .jpg so only work for jpeg files; "wb+" works with incoming binary file and write that file to "temp/" location; dest = destination
#         for chunk in file.chunks():#chunks() method reads the file(we received as parameter) in chunk instead read in one go becuase reading in chunk is efficient
#             dest.write(chunk) #write that file chunk by chunk in that destination

# class CreateProfileView(View):
#     # def get(self, request):
#     #     return render(request, "profiles/create_profile.html")

#     # def post(self, request):
#     #    store_file(request.FILES["image"]) #this is for file data and key ["image"] to access that specific data/file and access for all the non file data "request.POST"
#     #    return HttpResponseRedirect("/profiles")

#     #using forms.py
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form" : form
#         })
    
#     # def post(self, request):
#     #    submitted_form = ProfileForm(request.POST, request.FILES) #request.POST = submitted data; request.FILES = submitted file
       
#     #    if submitted_form.is_valid():
#     #         store_file(request.FILES["image"])
#     #         return HttpResponseRedirect("/profiles")
       
#     #    #if submitted_form is invalid
#     #    return render(request, "profiles/create_profile.html", {
#     #         "form" : submitted_form
#     #     })

#     #usring models.py
#     def post(self, request):
#        submitted_form = ProfileForm(request.POST, request.FILES) #request.POST = submitted data; request.FILES = submitted file
       
#        if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"]) #"image=" field is from image.py, "user_image" is from forms.py(form class) because out from is render with the help of form class and that class uses user_image as a field name for the FileField so that is then the key by which we can retreive the file
#            #we access "user_image" filed in the incomming file "request.FILES" and store it as a value in the "image="" field of the "UserProfile" class
            
#             profile.save()#we do not need to manually store that file now
#             return HttpResponseRedirect("/profiles")
       
       
#        return render(request, "profiles/create_profile.html", {
#             "form" : submitted_form
#         })


#using CreateView; we donot need above class; all we need is the "model" 
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields= "__all__"
    success_url = "/profiles"


#to show/display the files
class ProfilesView(ListView):
    model = UserProfile
    template_name= 'profiles/user_profiles.html'
    context_object_name = "profiles" #this "profiles" is passed to 'profiles/user_profiles.html'



   