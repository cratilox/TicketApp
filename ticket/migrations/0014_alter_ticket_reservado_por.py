# Generated by Django 4.2.5 on 2023-11-18 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0013_alter_ticket_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='reservado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]