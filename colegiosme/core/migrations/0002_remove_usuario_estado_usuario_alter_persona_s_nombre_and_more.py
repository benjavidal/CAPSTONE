# Generated by Django 5.1 on 2024-10-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='estado_usuario',
        ),
        migrations.AlterField(
            model_name='persona',
            name='s_nombre',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.DeleteModel(
            name='EstadoUsuario',
        ),
    ]