# Generated by Django 4.2.11 on 2024-03-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_subsection_slogan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='slogan',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]