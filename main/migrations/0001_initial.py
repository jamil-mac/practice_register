# Generated by Django 4.2.11 on 2024-03-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(db_index=True, max_length=255, verbose_name='faculty_name')),
                ('abbreviation', models.CharField(blank=True, max_length=30, null=True, verbose_name='abbreviation')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'faculty',
                'verbose_name_plural': 'faculties',
            },
        ),
    ]
