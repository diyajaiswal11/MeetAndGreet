# Generated by Django 3.0.4 on 2020-03-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200329_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilepicture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
