# Generated by Django 3.1.7 on 2021-03-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_invoice_bankaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='is_credited',
            field=models.BooleanField(default=False),
        ),
    ]
