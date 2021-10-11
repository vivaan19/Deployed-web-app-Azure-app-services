from django.shortcuts import render ,HttpResponse

content={
    "variable":"<This is the value of this variable>"
}
def index(request):
    # return HttpResponse("Hello World Changed the home page of django !!!")
    return render(request, "index.html", content)
def about(request):
    return HttpResponse("This is about page !!!")

def contact(request):
    return HttpResponse("This is a contact page !!!")

# Create your views here.
