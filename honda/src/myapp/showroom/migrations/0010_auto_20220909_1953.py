# Generated by Django 2.2 on 2022-09-09 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0009_auto_20220909_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('pan', models.CharField(max_length=10)),
                ('adhaar', models.CharField(max_length=12, unique=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='VehicleNum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='showroom.vehicle'),
        ),
        migrations.CreateModel(
            name='booking_by_staff',
            fields=[
                ('bookingid', models.IntegerField(primary_key=True, serialize=False)),
                ('staffid', models.ForeignKey(on_delete=None, to='showroom.staff')),
                ('stockid', models.ForeignKey(on_delete=None, to='showroom.stock')),
            ],
        ),
        migrations.CreateModel(
            name='booking_by_customer',
            fields=[
                ('custid', models.IntegerField(primary_key=True, serialize=False)),
                ('staffid', models.ForeignKey(on_delete=None, to='showroom.staff')),
                ('stockid', models.ForeignKey(on_delete=None, to='showroom.stock')),
            ],
        ),
    ]