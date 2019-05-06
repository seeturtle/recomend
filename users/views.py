from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from polls.models import Question


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def index(request):
    latest_question_list = Question.objects.order_by('-created_at')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'users/index.html', context)


def mypage(request):
    return render(request, 'users/mypage.html')
