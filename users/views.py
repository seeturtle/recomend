from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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
