# Generated by Django 4.0.3 on 2023-04-15 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_donor_contact_alter_userdata_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
