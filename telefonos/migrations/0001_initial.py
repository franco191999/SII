# Generated by Django 4.1.1 on 2022-11-29 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono_Fijo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10, verbose_name='Numero')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidad.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Pizarra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=8, verbose_name='Numero')),
                ('troncos', models.IntegerField(verbose_name='Troncos')),
                ('marca', models.CharField(blank=True, max_length=128, null=True, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=128, null=True, verbose_name='Modelo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidad.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Extencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=6, verbose_name='Numero')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unidad.departamento')),
                ('pizarra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='telefonos.pizarra')),
            ],
        ),
    ]