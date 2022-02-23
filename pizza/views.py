from django.http import HttpResponse, HttpResponseNotFound

from .models import Pizza
import random

def index(request, pid):
	pizza1 = Pizza.objects.all()
	if pid <= len(pizza1):	
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
		
def random(request):
    pizza = Pizza.objects.order_by('?')[0]
    return HttpResponse(
        content={
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        }
    )
