# Generated by Django 4.1 on 2022-10-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Nombre", models.CharField(max_length=200)),
                ("ciudad", models.CharField(max_length=200)),
                ("cedula", models.CharField(max_length=200)),
                ("telefono", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo_pedido", models.CharField(max_length=200)),
                ("codigo_producto", models.CharField(max_length=200)),
                ("cantidad", models.IntegerField()),
                ("fecha", models.CharField(max_length=200)),
                ("descuento", models.IntegerField()),
                ("nombre_mesero", models.CharField(max_length=200)),
            ],
        ),
    ]
