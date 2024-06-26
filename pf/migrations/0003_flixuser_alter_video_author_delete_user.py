# Generated by Django 5.0.6 on 2024-06-08 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf', '0002_video_video_alter_video_author_alter_video_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlixUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pf.flixuser'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
