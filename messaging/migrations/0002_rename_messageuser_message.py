# Generated by Django 4.2.6 on 2024-03-05 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MessageUser',
            new_name='Message',
        ),
    ]
