# Generated by Django 5.0.1 on 2024-02-07 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0004_alter_payment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='name',
            new_name='names',
        ),
    ]
