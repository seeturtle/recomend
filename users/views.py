from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from .models import User

from polls.forms import *
from polls.models import *


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def mypage(request, username):
    user = User.objects.get(username=username)
    context = {'myuser': user}
    return render(request, 'users/mypage.html', context)



def questionEdit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question_form = QuestionForm
    tag_form = TagForm

    if request.method == "POST":
        question_form = QuestionForm(request.POST)

        tag_form = TagForm(request.POST)
        if question_form.is_valid() and tag_form.is_valid():
            question.title = question_form.cleaned_data['title']
            question.reason = question_form.cleaned_data['reason']
            question.save()
            tag_form.save()
            m = "success"
        else:
            m = "failes"

        return redirect('questionEdit', question_id=question_id)

    context = {
        'question': question,
        'question_form': question_form,
        'tag': tag_form,
    }

    return render(request, 'users/question_edit.html', context)


