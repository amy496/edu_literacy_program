# Generated by Django 3.2 on 2021-05-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lit_app', '0005_alter_testsubmission_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsubmission',
            name='end_time',
            field=models.DateTimeField(),
        ),
    ]