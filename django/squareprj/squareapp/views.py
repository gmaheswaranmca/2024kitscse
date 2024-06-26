from django.shortcuts import render

# Create your views here.
def square(req):
    return render(req,'square.html')