# Generated by Django 4.0.4 on 2022-05-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='image',
            new_name='photo',
        ),
    ]