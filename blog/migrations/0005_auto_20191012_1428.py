# Generated by Django 2.2.5 on 2019-10-12 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191012_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 14, 28, 12, 670718, tzinfo=utc)),
        ),
    ]