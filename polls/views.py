from django.shortcuts import render, get_object_or_404
from .models import Question
from .forms import *


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def post(request):
    # debug
    m = "initial"

    tagForm = TagForm
    if request.method == "POST":
        questionForm = QuestionForm(request.POST)

        tagForm = TagForm(request.POST)
        if questionForm.is_valid() and tagForm.is_valid():
            question = questionForm.save(commit=False)
            question.user = request.user
            question.save()
            tagForm.save()
            m = "success"
        else:
            m = "failes"

    else:
        questionForm = QuestionForm

    return render(request, 'polls/post.html', {'form': questionForm, 'tag': tagForm, 'm': m})
