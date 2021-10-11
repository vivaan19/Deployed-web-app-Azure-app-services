from django.shortcuts import render ,HttpResponse

def index(request):
    # return HttpResponse("Hello World Changed the home page of django !!!")
    return render(request, "index.htm")
def about(request):
    return HttpResponse("This is about page !!!")

def contact(request):
    return HttpResponse("This is a contact page !!!")

# Create your views here.
