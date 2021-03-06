# Generated by Django 3.1.7 on 2021-02-25 13:14

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo ?')),
            ],
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            bases=('core.base',),
        ),
        migrations.CreateModel(
            name='Serviço',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('servico', models.CharField(max_length=100, verbose_name='Serviço')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-status-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=13, verbose_name='Icone')),
            ],
            bases=('core.base',),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('image', stdimage.models.StdImageField(upload_to='equipe', verbose_name='Image')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargos', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
            bases=('core.base',),
        ),
    ]
