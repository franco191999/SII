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
            name='Enlaces_Institucionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(blank=True, max_length=256, verbose_name='institucion ')),
                ('numero_servicio', models.TextField(blank=True, max_length=200, verbose_name='numero_servicio')),
                ('ip_lan', models.CharField(blank=True, max_length=256, verbose_name='ip_lan')),
                ('ip_wan', models.CharField(blank=True, max_length=256, verbose_name='ip_wan')),
                ('velocidad', models.CharField(blank=True, max_length=256, verbose_name='velocidad')),
                ('observaciones', models.TextField(blank=True, max_length=256, null=True, verbose_name='observaciones')),
                ('municipio', models.ForeignKey(blank=True, max_length=256, on_delete=django.db.models.deletion.CASCADE, to='unidad.nom_municipio')),
            ],
        ),
    ]