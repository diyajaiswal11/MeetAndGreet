# Generated by Django 3.0.4 on 2020-03-29 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200329_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profilepicture',
        ),
    ]