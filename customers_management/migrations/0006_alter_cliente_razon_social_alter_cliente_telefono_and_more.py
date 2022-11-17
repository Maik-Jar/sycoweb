# Generated by Django 4.1.2 on 2022-11-17 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers_management', '0005_tipocliente_alter_cliente_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='customers_management.tipocliente'),
        ),
    ]