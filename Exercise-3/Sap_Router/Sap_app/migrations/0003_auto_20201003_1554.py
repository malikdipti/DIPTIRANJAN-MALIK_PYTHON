# Generated by Django 2.2.13 on 2020-10-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sap_app', '0002_auto_20201003_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router_details',
            name='loopback',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='router_details',
            name='router_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='type_of_router',
            name='sap_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
