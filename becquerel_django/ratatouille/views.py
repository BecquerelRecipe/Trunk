from django.http import HttpResponse

def index(request):
    return HttpResponse("Ratatouille says hello world!")
# Create your views here.
