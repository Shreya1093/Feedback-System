# Generated by Django 2.1.7 on 2019-09-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190915_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='content',
            field=models.TextField(),
        ),
    ]
