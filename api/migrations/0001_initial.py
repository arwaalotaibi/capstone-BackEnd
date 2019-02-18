# Generated by Django 2.1.7 on 2019-02-14 15:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('datecreate', models.DateField(auto_now_add=True)),
                ('datecreate2', models.DateTimeField(auto_now_add=True)),
                ('datenow', models.DateField(default=datetime.datetime.now)),
                ('time', models.TimeField(auto_now_add=True)),
                ('n_vote', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=254)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('date2', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('y', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='x',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question'),
        ),
    ]