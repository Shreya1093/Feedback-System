# Generated by Django 2.1.7 on 2019-09-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='questionid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
