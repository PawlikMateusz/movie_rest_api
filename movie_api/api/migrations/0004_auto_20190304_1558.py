# Generated by Django 2.0.13 on 2019-03-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190304_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Country',
            field=models.CharField(max_length=20),
        ),
    ]
