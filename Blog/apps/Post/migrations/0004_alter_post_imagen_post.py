# Generated by Django 5.2.4 on 2025-07-23 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_alter_post_imagen_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen_post',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
