# Generated by Django 2.1.7 on 2019-02-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190215_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='n_vote',
            field=models.IntegerField(default=0.00396235760277365),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]