# Generated by Django 3.2.8 on 2021-10-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]
