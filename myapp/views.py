from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('hello world')
def my_name(request):
    context = {'name': 'coleen '}
    return render(request, 'myapp/myapp.html',context)