# Generated by Django 3.0.5 on 2020-06-02 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content_management_portal', '0009_prefilledcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleanSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('PYTHON', 'PYTHON'), ('C', 'C'), ('CPP', 'CPP'), ('PYTHON36', 'PYTHON36'), ('PYTHON37', 'PYTHON37'), ('PYTHON38', 'PYTHON38'), ('PYTHON38_DATASCIENCE', 'PYTHON38_DATASCIENCE'), ('PYTHON38_AIML', 'PYTHON38_AIML')], max_length=100)),
                ('solution_content', models.TextField()),
                ('file_name', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clean_solutions', to='content_management_portal.Question')),
            ],
        ),
    ]
