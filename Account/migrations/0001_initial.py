# Generated by Django 4.0 on 2022-01-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calculated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_weight', models.IntegerField(max_length=1000)),
                ('height', models.IntegerField(max_length=1000)),
                ('age', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_weight', models.IntegerField(max_length=1000)),
                ('height', models.IntegerField(max_length=1000)),
                ('age', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='weights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exe_name', models.TextField(max_length=200)),
                ('reps', models.IntegerField(max_length=100)),
                ('sets', models.IntegerField(max_length=10)),
                ('rpe', models.IntegerField(max_length=10)),
                ('weight', models.IntegerField(max_length=5000)),
                ('volume', models.IntegerField()),
            ],
        ),
    ]