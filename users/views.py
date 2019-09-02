from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from polls.forms import *
from polls.models import *
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from .models import User


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



def recommendEdit(request, recommend_id):

    recommend = get_object_or_404(Recommend, pk=recommend_id)
    recommend_form = RecommendForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and recommend_form.is_valid():

        recommend.name = recommend_form.cleaned_data['name']
        recommend.reason = recommend_form.cleaned_data['reason']
        recommend.image = recommend_form.cleaned_data['image']
        recommend.link = recommend_form.cleaned_data['link']
        recommend.save()
        return redirect('recommendEdit', recommend_id=recommend.id)

    context = {
        'recommend': recommend,
        'recommend_form': recommend_form,
    }

    return render(request, 'users/recommend_edit.html', context)


class UserChangeView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('edit_profile')

    def get_object(self, queryset=None):
        return self.request.user

