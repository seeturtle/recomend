from django.forms import ModelForm
from .models import *


class TagForm(ModelForm):
    """
    タグ用フォーム
    """

    class Meta:
        model = Tag
        fields = ['name']


class QuestionForm(ModelForm):
    """
    質問投稿フォーム
    """

    class Meta:
        model = Question
        fields = ['title', 'reason', 'tags']
        exclude = ['tags']


class RecommendForm(ModelForm):
    """
    レコメンド投稿フォーム
    """

    class Meta:
        model = Recommend
        fields = ['name', 'reason', 'image', 'link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'uk-input'})
        self.fields['reason'].widget.attrs.update({'class': 'uk-textarea', 'rows': 8})
        self.fields['link'].widget.attrs.update({'class': 'uk-input'})


class CommentForm(ModelForm):
    """
    コメント投稿フォーム
    """

    class Meta:
        model = Comment
        fields = ['contents']
