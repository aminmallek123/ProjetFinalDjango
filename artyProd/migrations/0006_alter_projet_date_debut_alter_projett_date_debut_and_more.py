# Generated by Django 4.1.7 on 2023-04-19 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artyProd', '0005_alter_projet_date_debut_projett'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='date_debut',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 19, 15, 50, 58, 476860)),
        ),
        migrations.AlterField(
            model_name='projett',
            name='date_debut',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 19, 15, 50, 58, 477859)),
        ),
        migrations.AlterField(
            model_name='projett',
            name='date_fin',
            field=models.DateField(max_length=12, null=True),
        ),
    ]
