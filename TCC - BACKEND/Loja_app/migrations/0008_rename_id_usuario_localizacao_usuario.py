# Generated by Django 5.0.8 on 2024-08-26 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loja_app', '0007_rename_usuario_localizacao_id_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localizacao',
            old_name='id_usuario',
            new_name='usuario',
        ),
    ]