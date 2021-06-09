from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Polls Index")

def home(request):
    return HttpResponse("Home Page")

def detail(request, question_id):
    return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
    response = "The results for question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s." % question_id)
