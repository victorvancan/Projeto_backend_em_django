# Generated by Django 3.1.7 on 2021-02-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210225_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='servicos',
            field=models.CharField(max_length=100, verbose_name='servicos'),
        ),
    ]
