from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def mypage(request, username):
    user = User.objects.get(username=username)
    context = {'myuser': user}
    return render(request, 'users/mypage.html', context)


class UserChangeView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('edit_profile')

    def get_object(self, queryset=None):
        return self.request.user
