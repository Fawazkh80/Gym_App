# Generated by Django 4.0 on 2022-01-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0003_inputweights_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputweights',
            name='calories_ate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
