from django.shortcuts import render, get_object_or_404

from questions.models import Question

def index(request):
	question_list = Question.objects.order_by('-pub_date')
	context = {'question_list': question_list}
	return render(request, 'questions/index.html', context);

def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'questions/question.html', {'question': question});
