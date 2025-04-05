# Generated by Django 5.2 on 2025-04-05 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaOutlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=300)),
                ('shares', models.IntegerField()),
                ('views', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MediaApp.mediaoutlet')),
            ],
        ),
    ]
