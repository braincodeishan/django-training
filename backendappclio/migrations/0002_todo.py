# Generated by Django 4.2.7 on 2023-11-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendappclio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
