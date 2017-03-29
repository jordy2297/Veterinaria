from django.shortcuts import render


def about(request):
	return render(request, "about.html", {})

def services(request):
	return render(request, "services.html", {})