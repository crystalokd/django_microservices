from django.http import HttpResponse, HttpResponseNotFound

from .models import Pizza

def index(request, pid):
	pizza = Pizza.objects.get(id=pid)
	if pizza:
		return HttpResponse(
			content={
				'id': pizza.id,
				'title': pizza.title,
				'description': pizza.description,
			}
		)
	else:
		return HttpResponseNotFound(
			content={
	 				"status": "error",
	 				"message": "pizza not found"
			}
		)
	
