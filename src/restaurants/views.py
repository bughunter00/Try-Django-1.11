from django.http import HttpResponse
from django.shortcuts import render
import random
from django.views import View
from django.views.generic import TemplateView

#funtcion based view

# def home(request):
# 	html_ = """
# 	<!DOCTYPE html>
# 	<html lang= pl>
# 	<head></head>
# 	<body>
#     <h1> Hello</h1>s
#     <p>this is html</p>
# 	</body>
# 	</html>
# 	"""s
# 	return HttpResponse(html_)
# 	#return render(request, "home.html", {})

# def home(request):
# 	num = None
# 	some_list = [
# 		random.randint(0, 100000), 
# 		random.randint(0, 100000), 
# 		random.randint(0, 100000), 
# 		random.randint(0, 100000)
# 	]
# 	condition_bool_item = True
# 	if condition_bool_item:
# 		num = random.randint(0, 100000)
# 	context = {
# 	    "html_var" : True,
# 	    "num" : num, 
# 	    "some_list": some_list
# 	}
# 	return render(request, "home.html", context)

# def about(request):
# 	context = {
# 	}
# 	return render(request, "about.html", context)

# def contact(request):
# 	context = {
	    
# 	}
# 	return render(request, "contact.html", context)

# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		# print(kwargs)
# 		context = {}
# 		return render(request, "contact.html", context)



class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		num = None
		some_list = [
			random.randint(0, 100000), 
			random.randint(0, 100000), 
			random.randint(0, 100000), 
			random.randint(0, 100000)
		]
		condition_bool_item = True
		if condition_bool_item:
			num = random.randint(0, 100000)
		context = {
	    	"html_var" : True,
	    	"num" : num, 
	    	"some_list": some_list
		}
		return context