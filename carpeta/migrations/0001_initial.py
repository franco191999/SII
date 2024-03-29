# Generated by Django 4.1.1 on 2022-11-29 05:25

import carpeta.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ancho_banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancho', models.CharField(blank=True, max_length=256, null=True, verbose_name='ancho')),
            ],
        ),
        migrations.CreateModel(
            name='Anno_unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anno', models.DateTimeField(auto_now_add=True, verbose_name='Anno')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=256, null=True, verbose_name='estado')),
            ],
        ),
        migrations.CreateModel(
            name='Conectividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_cuentas', models.IntegerField(blank=True, null=True)),
                ('unidad', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conectividades', to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetivo', models.TextField(blank=True, max_length=256, null=True, verbose_name='objetivo')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=256, null=True, verbose_name='tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.TextField(blank=True, max_length=256, null=True, verbose_name='resultado')),
                ('observaciones', models.TextField(blank=True, max_length=256, null=True, verbose_name='observaciones')),
                ('tipo', models.BooleanField(verbose_name='Tipo')),
                ('anno_unidad', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, to='carpeta.anno_unidad')),
                ('categoria', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, to='carpeta.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='P_web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('observaciones', models.TextField(blank=True, max_length=256, null=True, verbose_name='observaciones')),
                ('conectividad', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_web', to='carpeta.conectividad')),
                ('tipo', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, to='carpeta.tipo_web')),
            ],
        ),
        migrations.CreateModel(
            name='Ficheros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, max_length=256, null=True, verbose_name='nombre')),
                ('descripcion', models.TextField(blank=True, max_length=256, null=True, verbose_name='descripcion')),
                ('activo', models.BooleanField(verbose_name='activo')),
                ('unidad', models.ManyToManyField(to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='Enlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=256, null=True, verbose_name='Tipo de enlace')),
                ('acceso', models.BooleanField(verbose_name='Internet')),
                ('serv_ptes_ext', models.BooleanField(verbose_name='Paquetes')),
                ('ip', models.GenericIPAddressField()),
                ('ancho_banda', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, to='carpeta.ancho_banda')),
                ('conectividad', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enlacesXconectividad', to='carpeta.conectividad')),
            ],
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ficheros', models.FileField(blank=True, null=True, upload_to=carpeta.models.Documentos.get_upload_file_name)),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carpeta.ficheros')),
                ('unidad', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='Aplicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, max_length=256, null=True, verbose_name='Nombre')),
                ('comentario', models.TextField(blank=True, max_length=256, null=True, verbose_name='Comentario')),
                ('documento', models.FileField(blank=True, null=True, upload_to=carpeta.models.Aplicaciones.get_upload_file_name)),
                ('estado', models.BooleanField(verbose_name='Estado')),
                ('unidad', models.ManyToManyField(blank=True, max_length=256, to='unidad.unidad')),
            ],
        ),
        migrations.AddField(
            model_name='anno_unidad',
            name='objetivos',
            field=models.ManyToManyField(blank=True, max_length=256, to='carpeta.objetivo'),
        ),
        migrations.AddField(
            model_name='anno_unidad',
            name='unidad',
            field=models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad'),
        ),
    ]
