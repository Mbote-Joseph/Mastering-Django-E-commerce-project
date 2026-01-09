from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
# request -> response (One sends a request and receives a response)
# request handler
# action

def calculate():
    x = 10
    y = 20
    return x+y

def say_hello(request):
    # In the function you can:
    # - Pull data from db
    # - Transform
    # - send email
    query_set = Product.objects.all()
    return render(request, 'home.html', {'name': 'Joseph'})