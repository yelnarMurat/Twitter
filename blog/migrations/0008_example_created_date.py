# Generated by Django 2.0.1 on 2018-04-27 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
