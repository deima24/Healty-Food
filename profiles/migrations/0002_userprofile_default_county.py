# Generated by Django 4.2.1 on 2023-07-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
