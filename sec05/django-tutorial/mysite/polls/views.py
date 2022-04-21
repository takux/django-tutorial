from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "投票結果：{}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse(f'投票する質問：{question_id}')
