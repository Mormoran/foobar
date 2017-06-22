from django.shortcuts import render

# Create your views here.
def foobalicious(request):
    return render(request, 'index.html')