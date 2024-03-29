# Generated by Django 4.2.1 on 2023-07-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, choices=[('Avon', 'Avon'), ('Bedfordshire', 'Bedfordshire'), ('Berkshire', 'Berkshire'), ('Cambridgeshire', 'Cambridgeshire'), ('Buckinghamshire', 'Buckinghamshire'), ('Cheshire', 'Cheshire'), ('Cornwall', 'Cornwall'), ('Cumbria', 'Cumbria'), ('Derbyshire', 'Derbyshire'), ('Devon', 'Devon'), ('Dorset', 'Dorset'), ('Durham', 'Durham'), ('Essex', 'Essex'), ('Gloucestershire', 'Gloucestershire'), ('Hampshire', 'Hampshire'), ('Herefordshire', 'Herefordshire'), ('Hertfordshire', 'Hertfordshire'), ('Kent', 'Kent'), ('Lancashire', 'Lancashire')], max_length=80, null=True),
        ),
    ]
