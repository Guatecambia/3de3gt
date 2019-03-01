# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-01 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='authLetter',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='celphone',
            field=models.CharField(max_length=40, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='email',
            field=models.CharField(max_length=300, null=True, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='ethnicGroup',
            field=models.CharField(choices=[('I', 'Indígena'), ('ML', 'Mestizo/Ladino'), ('O', 'Otro')], max_length=2, null=True, verbose_name='Grupo étnico'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='ethnicOther',
            field=models.CharField(max_length=50, null=True, verbose_name='Especifique grupo étnico'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='facebook',
            field=models.CharField(max_length=200, null=True, verbose_name='Página de Facebook'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1, null=True, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='genderOther',
            field=models.CharField(max_length=50, null=True, verbose_name='Especifique género'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='helpCelphone',
            field=models.CharField(max_length=40, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='helpEmail',
            field=models.CharField(max_length=300, null=True, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='helpLastname',
            field=models.CharField(max_length=200, null=True, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='helpName',
            field=models.CharField(max_length=200, null=True, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='maritalStatus',
            field=models.CharField(choices=[('S', 'Soltero'), ('C', 'Casado'), ('UH', 'En unión de hecho'), ('O', 'Otro')], max_length=2, null=True, verbose_name='Estado Civil (al momento de presentar la declaración)'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='phone',
            field=models.CharField(max_length=40, null=True, verbose_name='Oficina/Casa'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='solvencia',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='webpage',
            field=models.CharField(max_length=300, null=True, verbose_name='Página Web'),
        ),
    ]
