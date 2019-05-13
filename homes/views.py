from django.shortcuts import render
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-created_at')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'homes/index.html', context)
