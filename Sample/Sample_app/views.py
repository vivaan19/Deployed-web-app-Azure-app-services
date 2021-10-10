from django.shortcuts import render ,HttpResponse

def index(request):
    return HttpResponse("Hello World Changed the home page of django !!!")

# Create your views here.
