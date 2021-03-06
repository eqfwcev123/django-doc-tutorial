from django.http import HttpResponse
from django.template import loader
from django.views import generic

from polls.models import Question, Choice
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # q를 순회 하면서 list 안에 q.question_text 를 넣어준다.
#     # output = ', '.join(q.question_text for q in latest_question_list)
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    # Use a default template name called <application name>/<model_name>_detail.html
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return the last five published questions
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    # used to tell Django to use a specific template name instead of the autogenerated
    # default template name
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    # used to tell Django to use a specific template name instead of the autogenerated
    # default template name
    # A different template name is given to ResultView in order to ensure that the results
    # view and the detail view have a different appearance when rendered, Eventhough they are bot DetailView
    template_name = 'polls/results.html'


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question,
#     }
#     return render(request, 'polls/detail.html', context)
#
#
# def results(request, question_id):
#     return HttpResponse(f'You are looking at the results of {question_id}')


def vote(request, pk):
    # question = get_object_or_404(Question, pk=pk)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     return render(request,
    #                   'polls/detail.html', {
    #                       'question': question,
    #                       'error_message': 'You did not select a choice'
    #                   })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    # return redirect('polls:results', question.id)
    if request.method == 'POST':
        try:
            choice_pk = request.POST['choice']  # 해당 choice의 id 번호를 가지고 온다
            choice = get_object_or_404(Choice, pk=choice_pk)  # 가지고온 id번호를 이용해서 정보를 가지고 온다
        except (KeyError, Choice.DoesNotExist):
            return redirect('polls:detail', pk=pk)  # 왼쪽에 있는 pk는 urlpatterns에 나와있는 pk 이다.
        else:
            choice.votes += 1  # 데이터베이스에 votes 의 값을 1 추가
            choice.save()
        return redirect('polls:results', pk=pk)


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/results.html', {'question': question})
