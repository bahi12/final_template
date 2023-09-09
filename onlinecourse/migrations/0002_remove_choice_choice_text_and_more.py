# Generated by Django 4.2.2 on 2023-09-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='submitted_on',
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='question title', max_length=550),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=5.0),
        ),
    ]
