from django.http import HttpResponse
from django.shortcuts import render
import random

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

def home(request):
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
	return render(request, "base.html", context)

def home2(request):
	context = {
	}
	return render(request, "home2.html", context)

def home3(request):
	context = {
	    
	}
	return render(request, "home3.html", context)