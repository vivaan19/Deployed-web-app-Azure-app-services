from django.shortcuts import render ,HttpResponse



def index(request):  # this returns to home page. 
    # return HttpResponse("Hello World Changed the home page of django !!!")
    return render(request, "base_myboot.html")
    
def about(request):
    # return HttpResponse("This is about page !!!")
    return render(request, "about.html")

def contact(request):
    # return HttpResponse("This is a contact page !!!")
    return render(request, "contact.html")

def services(request):
    return HttpResponse("This is services page !")
    # return render(request, "myboot_website.html")

# def connect(request):
#     return HttpResponse("This is connect with us page !")
    # return render(request, "myboot_website.html")
# Create your views here.
