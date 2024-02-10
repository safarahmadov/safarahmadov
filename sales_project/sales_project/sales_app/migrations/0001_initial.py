# Generated by Django 5.0.1 on 2024-02-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]