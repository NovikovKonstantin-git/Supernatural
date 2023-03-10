# Generated by Django 3.2.7 on 2021-10-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creatures',
            options={'ordering': ['title'], 'verbose_name': 'Cтатья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='creatures',
            name='content',
            field=models.TextField(blank=True, verbose_name='О существе'),
        ),
        migrations.AlterField(
            model_name='creatures',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано?'),
        ),
        migrations.AlterField(
            model_name='creatures',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='creatures',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
    ]
