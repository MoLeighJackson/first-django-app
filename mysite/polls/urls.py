from django.urls import path

from . import views

app_name = 'polls'
#wire poll/views.py views to urls
urlpatterns = [

    # polls view is index view
    path('', views.index, name='index'),
    # polls/question id num
    path('<int:question_id>/', views.detail, name='detail'),
    # polls/question id num/results
    path('<int:question_id>/results/', views.results, name='results'),
    # polls/question id num/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
