# Generated by Django 2.0.13 on 2019-03-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Actors',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='DVD',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Metascore',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Released',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Runtime',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Website',
            field=models.CharField(max_length=300),
        ),
    ]
