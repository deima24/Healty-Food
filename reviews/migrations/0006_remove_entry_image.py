# Generated by Django 4.2.1 on 2023-07-28 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_entry_entrytype_response_entry_entry_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='image',
        ),
    ]