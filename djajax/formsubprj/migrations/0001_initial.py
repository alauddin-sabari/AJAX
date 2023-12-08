# Generated by Django 4.1.4 on 2023-12-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=12)),
            ],
        ),
    ]
