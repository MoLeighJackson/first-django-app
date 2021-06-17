from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def home(request):
    return HttpResponse("Home Page")

def detail(request, question_id):
    return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
    response = "The results for question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s." % question_id)

