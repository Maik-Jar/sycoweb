# Generated by Django 4.1.2 on 2022-11-07 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_services_management', '0006_rename_descripcion_producto_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(default='service', max_length=90),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='detalle',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
