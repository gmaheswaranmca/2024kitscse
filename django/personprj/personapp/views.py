from django.shortcuts import render
from .models import Person 
# Create your views here.
def persons_list(req):
    persons = Person.objects.all()
    return render(req,'persons-list.html',{'persons':persons})
