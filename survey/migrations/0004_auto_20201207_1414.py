# Generated by Django 2.2.10 on 2020-12-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20201207_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_options',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='AnswerOption',
        ),
    ]
