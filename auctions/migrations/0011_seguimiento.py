# Generated by Django 4.2.3 on 2023-07-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_rename_comentador_id_comentario_comentario_id_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguido', models.BooleanField(default=False)),
                ('seguimiento_id_usuario', models.IntegerField()),
                ('seguimiento_id_producto', models.IntegerField()),
            ],
        ),
    ]
