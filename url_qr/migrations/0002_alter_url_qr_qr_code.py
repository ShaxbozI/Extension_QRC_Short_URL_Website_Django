# Generated by Django 4.2.7 on 2023-11-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_qr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_qr',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]
