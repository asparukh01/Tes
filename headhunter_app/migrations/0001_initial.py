# Generated by Django 4.0 on 2022-04-15 12:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import headhunter_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=20, verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Опыт работы')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=25, validators=[headhunter_app.validators.MinLengthValidator(3)], verbose_name='Название поля')),
                ('description', models.TextField(blank=True, max_length=500, null=True, validators=[headhunter_app.validators.WordLengthValidator(50)], verbose_name='Описание поля')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50, verbose_name='Название вакансии')),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Заработная плата')),
                ('description', models.TextField(blank=True, max_length=500, null=True, validators=[headhunter_app.validators.WordLengthValidator(50)], verbose_name='Детальное описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='headhunter_app.category', verbose_name='Категория')),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='headhunter_app.experience', verbose_name='Опыт работы')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50, validators=[headhunter_app.validators.MinLengthValidator(3)], verbose_name='Название задачи')),
                ('description', models.TextField(blank=True, max_length=500, null=True, validators=[headhunter_app.validators.WordLengthValidator(50)], verbose_name='Описание задачи')),
                ('telegram', models.CharField(blank=True, max_length=50, null=True, validators=[headhunter_app.validators.MinLengthValidator(3)], verbose_name='Телеграм')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('phone_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='Телефон')),
                ('facebook', models.CharField(blank=True, max_length=50, null=True, validators=[headhunter_app.validators.MinLengthValidator(3)], verbose_name='Facebook')),
                ('linkedin', models.CharField(blank=True, max_length=50, null=True, validators=[headhunter_app.validators.MinLengthValidator(3)], verbose_name='Linkedin')),
                ('infos', models.ManyToManyField(blank=True, related_name='infos', to='headhunter_app.Info', verbose_name='Дополнительная информация')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
