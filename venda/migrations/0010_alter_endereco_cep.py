# Generated by Django 4.2 on 2023-06-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0009_rename_país_endereco_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=8),
        ),
    ]
