# Generated by Django 4.2.3 on 2023-08-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0019_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='IsMarked',
            field=models.BooleanField(default=False),
        ),
    ]
