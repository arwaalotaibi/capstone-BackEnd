# Generated by Django 2.1.7 on 2019-02-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_vote_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='_type',
            field=models.CharField(choices=[('---', '__'), ('c1', 'C1'), ('c2', 'C2'), ('c3', 'C3'), ('c4', 'C4')], default='---', max_length=33),
        ),
    ]
