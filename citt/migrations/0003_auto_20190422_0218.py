# Generated by Django 2.2 on 2019-04-22 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citt', '0002_auto_20190421_0417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='evento_asisitio_alumno',
            new_name='evento_asistio_alumno',
        ),
    ]