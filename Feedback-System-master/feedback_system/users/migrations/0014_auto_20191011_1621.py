# Generated by Django 2.1.7 on 2019-10-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20191011_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=6),
        ),
    ]
