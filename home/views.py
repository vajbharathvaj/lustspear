from django.shortcuts import render


# Create your views here.
def home(request):
	context={'success':"we go it"}
	return render (request,'home/home_page.html',context)
def feed(request):
    context={'success':"we go it"}
    return render(request,'home/feed.html',context)