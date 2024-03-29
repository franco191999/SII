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
            name='nom_partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partida', models.CharField(max_length=25, verbose_name='Partida')),
                ('descripcion', models.TextField(blank=True, max_length=256, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='retiros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.CharField(max_length=25, verbose_name='Numero de factura')),
                ('importe', models.FloatField(max_length=256, verbose_name='Importe a Pagar')),
                ('detalles', models.TextField(blank=True, max_length=256, null=True)),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha del Retiro')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.nom_partida')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_inicial', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Presupuesto asignado')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha del Retiro')),
                ('unidad', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
    ]
