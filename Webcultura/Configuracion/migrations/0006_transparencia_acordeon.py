# Generated by Django 3.2 on 2022-11-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuracion', '0005_auto_20221118_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='transparencia',
            name='acordeon',
            field=models.CharField(default=1, help_text='Acordeon ', max_length=50, verbose_name='Acordeon  '),
            preserve_default=False,
        ),
    ]