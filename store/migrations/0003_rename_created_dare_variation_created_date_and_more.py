# Generated by Django 4.1.3 on 2023-03-13 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='created_dare',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='variation_valuse',
            new_name='variation_value',
        ),
    ]
