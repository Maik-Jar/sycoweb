# Generated by Django 4.1.2 on 2022-11-21 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers_management', '0006_alter_cliente_razon_social_alter_cliente_telefono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_documento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customers_management.tipodocumento'),
        ),
    ]