# Generated by Django 3.1.7 on 2021-02-25 17:30

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210225_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='ativo?'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='image',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='servicos',
            field=models.CharField(max_length=100, verbose_name='Serviços'),
        ),
    ]
