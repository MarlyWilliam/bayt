# Generated by Django 3.2.20 on 2023-08-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]