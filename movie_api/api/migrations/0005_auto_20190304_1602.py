# Generated by Django 2.0.13 on 2019-03-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190304_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Writer',
            field=models.CharField(max_length=300),
        ),
    ]
