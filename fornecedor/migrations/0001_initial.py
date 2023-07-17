# Generated by Django 4.2 on 2023-07-13 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venda', '0010_alter_endereco_cep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venda.endereco')),
            ],
        ),
    ]