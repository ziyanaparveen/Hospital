# Generated by Django 4.2.6 on 2023-10-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_image',
            field=models.ImageField(upload_to='doctors/'),
        ),
    ]