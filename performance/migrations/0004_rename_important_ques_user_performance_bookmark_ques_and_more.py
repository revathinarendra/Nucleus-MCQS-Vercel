# Generated by Django 5.0.4 on 2024-05-08 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0003_alter_user_performance_doubt_ques_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_performance',
            old_name='important_ques',
            new_name='bookmark_ques',
        ),
        migrations.RenameField(
            model_name='user_performance',
            old_name='doubt_ques',
            new_name='revise_ques',
        ),
        migrations.RemoveField(
            model_name='user_performance',
            name='star_ques',
        ),
    ]