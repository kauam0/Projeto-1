# Generated by Django 5.1.3 on 2024-11-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemprodutos',
            name='imagem',
            field=models.ImageField(upload_to='media'),
        ),
    ]
