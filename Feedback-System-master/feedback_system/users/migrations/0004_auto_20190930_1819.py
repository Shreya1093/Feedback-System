# Generated by Django 2.1.7 on 2019-09-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190930_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(max_length=1),
        ),
    ]