# Generated by Django 5.1.3 on 2024-11-18 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_imagemprodutos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemprodutos',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='produtos.produtos'),
        ),
    ]
