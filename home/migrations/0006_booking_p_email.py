# Generated by Django 4.2.6 on 2023-10-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='p_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
