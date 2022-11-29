from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, "templates/index.html")

def login(request):
    return render(request, "templates/login.html")

def user(request):
    return HttpResponse("WE ARE DEVELOPING IT !")

def request_page(request):
    print("Indide...")
    if(request.POST.post('submitlogin')):
        username = request.POST.get('myusername')
        password = request.POST.get('mypassword')
        print(username)
        print(password)
    return render(request,'templates/login.html')

