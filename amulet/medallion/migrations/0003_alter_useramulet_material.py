# Generated by Django 4.1.7 on 2023-06-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medallion', '0002_useramulet_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useramulet',
            name='material',
            field=models.CharField(max_length=30),
        ),
    ]