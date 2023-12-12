# Generated by Django 3.0.5 on 2020-06-03 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content_management_portal', '0010_cleansolution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint_number', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('content_type', models.CharField(choices=[('TEXT', 'TEXT'), ('HTML', 'HTML'), ('MARKDOWN', 'MARKDOWN')], max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hints', to='content_management_portal.Question')),
            ],
        ),
    ]