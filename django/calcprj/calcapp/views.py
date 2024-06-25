from django.shortcuts import render

# Create your views here.
def calc(req):
    if req.method == "POST":
        first = req.POST["first"]
        second = req.POST["second"]
        result = int(first) + int(second)        
    else:
        first = 0 
        second = 0 
        result = 0 
    return render(req,'calc.html',{'first':first,
                                   'second':second,
                                   'result':result})
