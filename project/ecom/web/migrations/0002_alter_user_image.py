# Generated by Django 5.1.6 on 2025-03-06 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='./default_profile_image.png', upload_to='media'),
        ),
    ]
