from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
	title = "hello there"
	context = {"title":title}
	if request.user.is_authenticated:
		context = {"title":title, "my_list": [1,2,3,4,5]}
	return render(request, "home.html", context )

def contact_page(request):
	return render(request, "helloworld.html", {"title":"About us"})

def about_page(request):
	return render(request, "about.html", {"title":"About"})


def example_page(request):
	context = {"title":"Example"}
	template_name = "helloworld.html"
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context)
	return HttpResponse(rendered_item) #render(request, "about.html", {"title":"About"})