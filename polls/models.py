from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Tag(models.Model):
    """
    タグモデル
    """

    # タグ名
    name = models.CharField(max_length=200)


class Question(models.Model):
    """
    質問モデル
    """

    # 質問ユーザ
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 質問タイトル (What is the best ~)
    title = models.CharField(max_length=200)
    # 質問理由
    reason = models.TextField()
    # タグ (複数可)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recommend(models.Model):
    """
    おすすめモデル
    """

    # おすすめユーザ
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 対象質問
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # おすすめ名
    name = models.CharField(max_length=200)
    # おすすめ理由
    reason = models.TextField()
    # イメージ (Option)
    image = models.ImageField(upload_to='images/', null=True)
    # リンク (Option)
    link = models.URLField(null=True)
    # グッド数
    good_count = models.IntegerField(default=0)
    # バッド数
    bad_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
    コメントモデル
    """

    # コメントユーザ
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 対象質問
    target_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 対象おすすめ (Option)
    target_recommend = models.ForeignKey(Recommend, on_delete=models.CASCADE, null=True)
    # 返信先コメント (リプライの場合)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE)
    # コメント内容
    contents = models.TextField()
    # グッド数
    good_count = models.IntegerField(default=0)
    # バッド数
    bad_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
