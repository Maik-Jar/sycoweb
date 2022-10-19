# Generated by Django 4.1.2 on 2022-10-18 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_services_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='detalle',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_services_management.item', unique=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_services_management.item', unique=True),
        ),
    ]