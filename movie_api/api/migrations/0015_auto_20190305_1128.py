# Generated by Django 2.0.13 on 2019-03-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190305_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
