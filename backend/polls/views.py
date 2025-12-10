from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")