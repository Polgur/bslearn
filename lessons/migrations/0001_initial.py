# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField()),
                ('link', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Книги (Видеокурсы)',
                'verbose_name': 'Книга (Видеокурс)',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.SmallIntegerField()),
                ('name', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField()),
                ('desc', models.TextField()),
                ('template', models.CharField(max_length=80)),
                ('prn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='lessons.Book')),
            ],
            options={
                'verbose_name_plural': 'Уроки',
                'verbose_name': 'Урок',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Теги',
                'verbose_name': 'Тег',
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, to='lessons.Tag'),
        ),
    ]