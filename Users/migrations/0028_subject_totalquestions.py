# Generated by Django 4.2.3 on 2023-12-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0027_remove_customuser_teststaken_resultsextradetails_bca_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='TotalQuestions',
            field=models.BigIntegerField(default=0),
        ),
    ]
