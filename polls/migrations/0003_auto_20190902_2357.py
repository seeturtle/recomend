# Generated by Django 2.2 on 2019-09-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_recommend_is_best'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='タグ名'),
        ),
    ]
