"""
Views de platzi
"""
from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))

def hi(request):
    """import pdb; pdb.set_trace()"""
    return HttpResponse('UOOOO')


def order_numbers(request):
	"""Get a list of numbers and return it numbers ordered as a JSon response."""
	numbers = request.GET.get('numbers')

	if isinstance(numbers, str):
		# parse string as list
		numbers = numbers.split(',')
		# parse all list values as int
		numbers = [int(number) for number in numbers]

	if isinstance(numbers, list):
		numbers = sorted(numbers)

	return JsonResponse({'ordered_numbers': numbers})

def order_numbers_solucion_oficial(request):
	"""Get a list of numbers and return it numbers ordered as a JSon response."""
	numbers = request.GET.get('numbers')

	if isinstance(numbers, str):
		# parse string as list
		numbers = numbers.split(',')
		# parse all list values as int
		numbers = [int(number) for number in numbers]

	if isinstance(numbers, list):
		numbers = sorted(numbers)

	return JsonResponse({'ordered_numbers': numbers})

def say_hi(request, name, age):
	"""exemplre url amb paràmetres"""
	if age < 12:
		message = 'Merda {}'.format(name)
	else:	
		message = 'Merda else {}'.format(name)
	return HttpResponse(message)