# Generated by Django 5.1.7 on 2025-04-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_inventory_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
