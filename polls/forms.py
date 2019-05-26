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


class CommentForm(ModelForm):
    """
    コメント投稿フォーム
    """

    class Meta:
        model = Comment
        fields = ['contents']
