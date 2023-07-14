# Generated by Django 4.2.3 on 2023-07-13 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_rename_comentario_id_usuario_comentario_comentador_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_seguimiento', models.BooleanField(default=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
