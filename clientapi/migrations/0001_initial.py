# Generated by Django 5.0.2 on 2024-02-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=100)),
                ('totalSpace', models.IntegerField(max_length=100)),
                ('usedSpace', models.IntegerField(max_length=100)),
                ('freeSpace', models.IntegerField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]