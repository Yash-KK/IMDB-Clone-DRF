# Generated by Django 4.0.4 on 2022-05-31 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0008_rename_user_review_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='num_rating',
            field=models.IntegerField(default=0),
        ),
    ]