# Generated by Django 2.2 on 2022-09-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0013_booking_by_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vtype',
            field=models.CharField(choices=[('2', 'Two-wheeler'), ('4', 'Four-wheeler')], max_length=20),
        ),
        migrations.DeleteModel(
            name='booking_by_admin',
        ),
    ]
