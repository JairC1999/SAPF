# Generated by Django 4.1 on 2022-10-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_testmodel_test2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Primeiro nome')),
                ('last_name', models.CharField(max_length=30, verbose_name='Segundo nome')),
                ('telefone', models.CharField(max_length=19, null=True, verbose_name='Telefone')),
            ],
        ),
    ]
