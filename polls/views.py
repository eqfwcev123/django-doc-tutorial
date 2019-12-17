from django.http import HttpResponse
from django.template import loader

from .models import Question, Choice
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # q를 순회 하면서 list 안에 q.question_text 를 넣어준다.
    # output = ', '.join(q.question_text for q in latest_question_list)
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    return HttpResponse(f'You are looking at the results of {question_id}')


def vote(request, question_id):
    return HttpResponse(f"you are voting on question {question_id}")
