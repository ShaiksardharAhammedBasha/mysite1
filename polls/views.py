from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.views import generic


def welcome(request):

	res = "Welcome to Django"

	return HttpResponse(res);


def hello(request):

	res = "Welcome to Django Project";
	return HttpResponse(res);

class IndexView(generic.ListView):

	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'


	def get_query(self):
		'''return the last five published questions.'''
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def detail(request, question_id):


	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):

	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})




def vote(request, question_id):

	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',
			{
			'question' : question,
			'error_message': "You didn't select a choice.",
			})

	else:
		selected_choice.votes += 1
		selected_choice.save()


		return HttpResponseRedirect(reverse('polls:results',
			args=(question.id, )))	










