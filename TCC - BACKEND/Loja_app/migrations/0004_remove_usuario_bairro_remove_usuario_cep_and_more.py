# Generated by Django 5.0.8 on 2024-08-21 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loja_app', '0003_usuario_bairro_usuario_cep_usuario_numero_casa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='numero_casa',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rua',
        ),
        migrations.CreateModel(
            name='localizacao',
            fields=[
                ('id_localizacao', models.AutoField(primary_key=True, serialize=False)),
                ('cep', models.IntegerField()),
                ('bairro', models.TextField(max_length=255)),
                ('rua', models.TextField(max_length=255)),
                ('numero_casa', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Loja_app.usuario')),
            ],
        ),
    ]