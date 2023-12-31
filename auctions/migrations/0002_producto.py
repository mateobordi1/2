# Generated by Django 4.2.3 on 2023-07-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('descripcion', models.CharField(max_length=512)),
                ('precioinicial', models.IntegerField()),
                ('imagenurl', models.CharField(max_length=128)),
                ('categoria', models.CharField(max_length=64)),
            ],
        ),
    ]
