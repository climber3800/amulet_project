# Generated by Django 4.1.7 on 2023-06-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medallion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useramulet',
            name='material',
            field=models.CharField(default='default', max_length=30),
        ),
    ]