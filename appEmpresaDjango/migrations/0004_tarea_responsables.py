# Generated by Django 5.2.1 on 2025-06-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresaDjango', '0003_alter_tarea_empleados'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='responsables',
            field=models.ManyToManyField(blank=True, related_name='proyectos_responsables', to='appEmpresaDjango.empleado'),
        ),
    ]
