# Generated by Django 3.2 on 2022-11-20 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuracion', '0006_transparencia_acordeon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre ', max_length=50, verbose_name='Nombre ')),
                ('imagen', models.ImageField(help_text='Imagen ', upload_to='', verbose_name='Imagen ')),
                ('descripcion', models.TextField(blank=True, help_text='Descripción', null=True, verbose_name='Descripción')),
                ('tipo', models.CharField(blank=True, choices=[('PRINCIPAL', 'PRINCIPAL'), ('SECUNDARIO', 'SECUNDARIO')], max_length=30, null=True, verbose_name='Estado:')),
                ('url', models.TextField(blank=True, null=True, verbose_name='URL Document')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': ('Slider',),
                'verbose_name_plural': 'Slider',
                'ordering': ['id'],
            },
        ),
    ]