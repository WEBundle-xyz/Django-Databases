from django.shortcuts import render
from .models import Members
from .forms import MemberForm 

def home(request):
    all_members = Members.objects.all
    return render(request, 'home.html', {'all': all_members})

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'join.html', {})
    else:
        return render(request, 'join.html', {})


