from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    カスタムユーザモデル
    """

    icon = models.ImageField('アイコン', upload_to='icons/', blank=True, default='icons/default.jpg')
    profile = models.CharField('プロフィール', max_length=200, blank=True, null=True)
