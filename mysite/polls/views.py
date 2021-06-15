from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    #display latest 10 polls questions on the index page
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    #separate poll questions with *
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,
            }
    return HttpResponse(template.render(context, request))

def home(request):
    return HttpResponse("Home Page")

def detail(request, question_id):
    return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
    response = "The results for question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s." % question_id)

