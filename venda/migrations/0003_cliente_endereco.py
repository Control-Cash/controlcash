# Generated by Django 4.2 on 2023-06-22 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0002_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='venda.endereco'),
        ),
    ]
