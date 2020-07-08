# Generated by Django 3.0.7 on 2020-07-08 14:22

from django.db import migrations
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200707_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False),
        ),
    ]
