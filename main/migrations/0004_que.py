# Generated by Django 2.2.1 on 2019-06-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190603_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='que',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=120)),
            ],
        ),
    ]
