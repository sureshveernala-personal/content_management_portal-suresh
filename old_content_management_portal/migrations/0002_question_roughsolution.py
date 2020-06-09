# Generated by Django 3.0.5 on 2020-05-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_text', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('content_type', models.CharField(choices=[('Text', 'text'), ('HTML', 'html'), ('Markdown', 'mark_down')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RoughSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('PYTHON', 'python'), ('C', 'c_language'), ('CPP', 'c_plus_plus'), ('PYTHON36', 'python36'), ('PYTHON37', 'python37'), ('PYTHON38', 'python38'), ('PYTHON38_DATASCIENCE', 'python38_datascience'), ('PYTHON38_AIML', 'python38_aiml')], max_length=100)),
                ('solution_content', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=100)),
            ],
        ),
    ]
