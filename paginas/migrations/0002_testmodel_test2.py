# Generated by Django 4.1 on 2022-10-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='test2',
            field=models.CharField(blank=True, max_length=50, verbose_name='teste2'),
        ),
    ]
