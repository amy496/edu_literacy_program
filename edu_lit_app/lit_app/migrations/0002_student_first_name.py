# Generated by Django 3.2 on 2021-04-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lit_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
            
        ),
    ]
