from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,'core/home.html')
def cv(request):
    return render(request,'core/cv.html')

def contact(request):
    return render(request,'core/contact.html')  
# Create your views here.
