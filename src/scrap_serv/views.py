import datetime
from django.shortcuts import render

def home(request):
    date  = datetime.datetime.now().date()
    name  = 'Alex'
    _dict = {'name': name, 'date': date}
    return render(request, 'home.html', _dict)