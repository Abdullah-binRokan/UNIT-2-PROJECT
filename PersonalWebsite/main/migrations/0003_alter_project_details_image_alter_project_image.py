# Generated by Django 4.2.16 on 2024-11-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_details_image_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='details_image',
            field=models.ImageField(default='default.jpg', upload_to='projects/images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='projects/images'),
        ),
    ]