from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    fields = UserCreationForm.Meta.fields + ('icon', 'profile')


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('icon', 'username', 'first_name', 'last_name', 'email', 'profile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'uk-input uk-form-width-large'
        self.fields['first_name'].widget.attrs['class'] = 'uk-input uk-form-width-large'
        self.fields['last_name'].widget.attrs['class'] = 'uk-input uk-form-width-large'
        self.fields['email'].widget.attrs['class'] = 'uk-input uk-form-width-large'
        self.fields['profile'].widget.attrs.update({'class': 'uk-textarea', 'rows': 8})
