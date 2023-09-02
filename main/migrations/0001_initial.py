# Generated by Django 4.2.4 on 2023-09-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('serial_num', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=15)),
            ],
        ),
    ]