"""platzigram views """

#django
from django.http import HttpResponse
#django utilities
from datetime import datetime
import json

def hello_world (request):
    """return a greeting"""
    now = datetime.now().strftime('%b %dth %y %H %M')
    return HttpResponse('oh mi current server is {now}'.format(now=str(now)))

def hi (request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_intd = sorted(numbers)
    data= {
        'status': 'ok',
        'numbers': sorted_intd,
        'message': 'integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data, indent=2), content_type='application/json')

def ages (request, name, age):
    if age > 18:
        message = 'hola {} bienvenido a platzigram]' \
                  ''.format(name)
    else:
        message = 'hola {} pero no pudes ingresar'.format(name)
    return HttpResponse(message)