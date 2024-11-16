# Generated by Django 4.2.16 on 2024-11-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='project/images')),
            ],
        ),
    ]
