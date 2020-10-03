# Generated by Django 2.2.13 on 2020-10-03 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type_of_Router',
            fields=[
                ('sap_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('router_type', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Router_Details',
            fields=[
                ('router_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('loopback', models.FloatField()),
                ('hostname', models.CharField(max_length=50, unique=True)),
                ('sap_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sap_app.Type_of_Router')),
            ],
        ),
    ]