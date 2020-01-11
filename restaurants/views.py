from django.shortcuts import render

# Create your views here.
def blah(request):
	return render(request, "blah.html", {"msg": "Hello World!"})