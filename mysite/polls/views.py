from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Polls Index")

def home(request):
    return HttpResponse("Home Page")
