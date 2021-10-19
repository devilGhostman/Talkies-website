# Generated by Django 3.2.8 on 2021-10-19 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='moviefiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('download', models.URLField()),
                ('duration', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=20)),
                ('imdb_rating', models.DecimalField(decimal_places=1, max_digits=10)),
                ('poster', models.URLField()),
                ('stream', models.URLField()),
                ('trailer', models.URLField()),
                ('user_rating', models.DecimalField(decimal_places=1, max_digits=10)),
                ('views', models.IntegerField()),
                ('year', models.IntegerField()),
                ('summary', models.TextField(max_length=500)),
                ('movie_id', models.IntegerField(default=1)),
            ],
        ),
    ]
