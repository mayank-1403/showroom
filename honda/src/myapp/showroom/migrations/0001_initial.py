# Generated by Django 2.2 on 2022-09-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('pan', models.CharField(max_length=10)),
                ('adhaar', models.CharField(max_length=12)),
                ('id', models.PositiveIntegerField(max_length=20, primary_key=True, serialize=False)),
                ('phone', models.PositiveIntegerField(max_length=10)),
            ],
        ),
    ]