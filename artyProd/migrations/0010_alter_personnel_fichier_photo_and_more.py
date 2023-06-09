# Generated by Django 4.1.7 on 2023-05-01 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artyProd', '0009_alter_projet_date_debut_alter_projett_date_debut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='fichier_photo',
            field=models.FileField(default='user.png', upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='date_debut',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 1, 1, 3, 40, 35745)),
        ),
        migrations.AlterField(
            model_name='projett',
            name='date_debut',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 1, 1, 3, 40, 36744)),
        ),
    ]
