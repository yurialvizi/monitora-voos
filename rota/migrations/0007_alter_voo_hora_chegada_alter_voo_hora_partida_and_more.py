# Generated by Django 4.1.3 on 2022-12-04 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0006_alter_voo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='hora_chegada',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voo',
            name='hora_partida',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voo',
            name='status',
            field=models.CharField(blank=True, choices=[('em', 'embarcando'), ('ca', 'cancelado'), ('pr', 'programado'), ('ta', 'taxiando'), ('pt', 'pronto'), ('ao', 'autorizado'), ('vo', 'em_voo'), ('at', 'aterrisado')], max_length=2, null=True),
        ),
    ]
