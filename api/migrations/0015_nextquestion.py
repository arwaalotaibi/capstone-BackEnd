# Generated by Django 2.1.7 on 2019-02-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_question_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='NextQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
