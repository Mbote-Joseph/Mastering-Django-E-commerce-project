from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response (One sends a request and receives a response)
# request handler
# action

def say_hello(request):
    # In the function you can:
    # - Pull data from db
    # - Transform
    # - send email
    return render(request, 'home.html')