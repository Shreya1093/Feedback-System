# Generated by Django 2.1.7 on 2019-09-23 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190923_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='PAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='POquestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pquestion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgramOutcomess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('poutcome', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='poquestions',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ProgramOutcomess'),
        ),
        migrations.AddField(
            model_name='panswers',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.ProgramOutcomess'),
        ),
    ]