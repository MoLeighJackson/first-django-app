from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# home page
def home(request):
    return HttpResponse("Home Page")

# poll page
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# detail view
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# results view
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# vote view
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # returns the ID of the selected choice, as a string
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # vote counting functionality
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        # after a user votes, redirect to the results page for the question
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))