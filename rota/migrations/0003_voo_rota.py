# Generated by Django 4.1.1 on 2022-10-06 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0002_alter_rota_hora_chegada_prevista_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='voo',
            name='rota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rota.rota'),
        ),
    ]