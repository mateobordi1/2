# Generated by Django 4.2.3 on 2023-07-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_seguimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento',
            name='en_seguimiento',
            field=models.BooleanField(),
        ),
    ]
