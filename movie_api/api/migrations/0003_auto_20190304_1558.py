# Generated by Django 2.0.13 on 2019-03-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190304_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbVotes',
            field=models.CharField(max_length=30),
        ),
    ]
