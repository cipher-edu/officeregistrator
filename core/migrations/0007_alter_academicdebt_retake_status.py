# Generated by Django 5.1.7 on 2025-03-26 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_subject_student_academicdebt_financeservice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdebt',
            name='retake_status',
            field=models.CharField(choices=[('Kutilmoqda', 'Kutilmoqda'), ('To‘langan', 'To‘langan'), ('Qayta topshirilgan', 'Qayta topshirilgan')], default='pending', max_length=50),
        ),
    ]
