# Generated by Django 3.2.6 on 2021-08-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acceuil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
