# Generated by Django 2.0.13 on 2019-03-04 13:44

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Year', models.PositiveIntegerField()),
                ('Rated', models.CharField(max_length=20)),
                ('Released', models.DateField()),
                ('Runtime', models.IntegerField()),
                ('Genre', models.CharField(max_length=100)),
                ('Director', models.CharField(max_length=100)),
                ('Writer', models.CharField(max_length=100)),
                ('Actors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('Plot', models.TextField()),
                ('Language', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=5)),
                ('Awards', models.CharField(max_length=50)),
                ('Poster', models.URLField()),
                ('Metascore', models.IntegerField()),
                ('imdbRating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('imdbVotes', models.IntegerField()),
                ('imdbID', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=30)),
                ('DVD', models.DateField()),
                ('BoxOffice', models.CharField(max_length=100)),
                ('Production', models.CharField(max_length=50)),
                ('Website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Source', models.CharField(max_length=100)),
                ('Value', models.CharField(max_length=10)),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api.Movie')),
            ],
        ),
    ]
