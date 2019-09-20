# Generated by Django 2.1.7 on 2019-09-20 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseOutcomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('questionid', models.IntegerField()),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CourseOutcomes')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CourseOutcomes')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='subid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Subject'),
        ),
        migrations.AddField(
            model_name='answers',
            name='courseid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.CourseOutcomes'),
        ),
        migrations.AddField(
            model_name='answers',
            name='questionid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='subid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Subject'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]