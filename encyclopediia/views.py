from django.shortcuts import render
from . import utill
# Create your views here.

def index(request):
    return render(request, 'encyclopedia/index.html',{
        'entries': utill.list_entries()
    })