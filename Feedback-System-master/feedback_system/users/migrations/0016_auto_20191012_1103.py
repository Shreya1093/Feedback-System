# Generated by Django 2.1.7 on 2019-10-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20191011_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poquestions',
            name='pquestion',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=2000),
        ),
    ]
