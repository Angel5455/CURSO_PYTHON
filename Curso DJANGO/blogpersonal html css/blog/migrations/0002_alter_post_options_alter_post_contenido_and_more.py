# Generated by Django 4.1.3 on 2022-11-19 18:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-fecha_creacion'], 'verbose_name': ('Publicacion',), 'verbose_name_plural': 'Publicaciones'},
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_act',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]