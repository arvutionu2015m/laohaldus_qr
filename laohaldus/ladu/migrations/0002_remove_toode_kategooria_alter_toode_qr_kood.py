# Generated by Django 5.1.7 on 2025-03-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toode',
            name='kategooria',
        ),
        migrations.AlterField(
            model_name='toode',
            name='qr_kood',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes'),
        ),
    ]
