# Generated by Django 2.2.1 on 2019-06-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_que'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='use',
            field=models.BooleanField(default=True),
        ),
    ]