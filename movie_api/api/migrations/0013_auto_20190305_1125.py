# Generated by Django 2.0.13 on 2019-03-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190305_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbRating',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
