# Generated by Django 4.1.5 on 2023-06-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_customuser_profileimage_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ProfileImage',
            field=models.ImageField(blank=True, default='pp-female.jpg', null=True, upload_to='0b12362e39c54baa9a917eb662225b5b/profile/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default='0b12362e39c54baa9a917eb662225b5b', editable=False, primary_key=True, serialize=False),
        ),
    ]
