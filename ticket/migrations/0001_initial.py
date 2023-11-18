# Generated by Django 4.2.5 on 2023-10-06 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=40, verbose_name='Destino de parada')),
                ('origen', models.CharField(max_length=40, verbose_name='Origen de parada')),
                ('salida', models.DateTimeField(verbose_name='Momento de salida')),
                ('bus', models.CharField(max_length=50, verbose_name='Matricula del bus')),
                ('compannia', models.CharField(max_length=40, verbose_name='Compañia de viaje')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
