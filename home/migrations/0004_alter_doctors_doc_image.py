# Generated by Django 4.2.6 on 2023-10-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_doctors_doc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_image',
            field=models.ImageField(upload_to='doctors'),
        ),
    ]
