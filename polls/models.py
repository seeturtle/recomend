from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Tag(models.Model):
    """
    タグモデル
    """

    name = models.CharField('タグ名', max_length=200)


class Question(models.Model):
    """
    質問モデル
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='質問ユーザ')
    title = models.CharField('質問タイトル', max_length=200)
    reason = models.TextField('質問理由')
    tags = models.ManyToManyField(Tag, verbose_name='タグ')

    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)


class Recommend(models.Model):
    """
    おすすめモデル
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='おすすめユーザ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='対象質問')
    name = models.CharField('おすすめ名', max_length=200)
    reason = models.TextField('おすすめ理由')
    image = models.ImageField('イメージ', upload_to='images/', blank=True, null=True)
    link = models.URLField('リンク', blank=True, null=True)
    good_count = models.IntegerField('グッド数', default=0)
    bad_count = models.IntegerField('バッド数', default=0)

    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)


class Comment(models.Model):
    """
    コメントモデル
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='コメントユーザ')
    target_question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='対象質問')
    target_recommend = models.ForeignKey(Recommend, on_delete=models.CASCADE, blank=True, null=True,
                                         verbose_name='対象おすすめ')
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='返信先コメント')
    contents = models.TextField('コメント内容')
    good_count = models.IntegerField('グッド数', default=0)
    bad_count = models.IntegerField('バッド数', default=0)

    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)
