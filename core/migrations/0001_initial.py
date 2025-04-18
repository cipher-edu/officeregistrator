# Generated by Django 5.1.7 on 2025-03-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('faculty', models.CharField(blank=True, max_length=200, null=True)),
                ('group', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
