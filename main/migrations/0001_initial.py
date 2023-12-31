# Generated by Django 4.1.6 on 2023-04-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_blog', models.IntegerField(null=True, verbose_name='Номер новости')),
                ('title', models.CharField(max_length=120, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d', verbose_name='Изображение')),
                ('description', models.CharField(max_length=350, null=True, verbose_name='Описание')),
                ('date', models.DateField(null=True, verbose_name='Дата публикации')),
                ('user', models.CharField(max_length=21, null=True, verbose_name='Опубликовал')),
            ],
            options={
                'verbose_name': 'Весть',
                'verbose_name_plural': 'Вести',
            },
        ),
    ]
