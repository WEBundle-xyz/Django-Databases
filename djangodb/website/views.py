from django.shortcuts import render
from .models import Members

def home(request):
    all_members = Members.objects.all
    return render(request, 'home.html', {'all': all_members})

def join(request):
    return render(request, 'join.html', {})


