# Generated by Django 5.1.7 on 2025-03-12 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladu', '0002_remove_toode_kategooria_alter_toode_qr_kood'),
    ]

    operations = [
        migrations.AddField(
            model_name='toode',
            name='kategooria',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='ladu.tootekategooria'),
            preserve_default=False,
        ),
    ]
