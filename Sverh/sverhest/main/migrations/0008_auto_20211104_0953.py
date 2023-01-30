# Generated by Django 3.2.7 on 2021-11-04 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20211031_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['author'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Автор комментария'),
        ),
        migrations.AlterField(
            model_name='creatures',
            name='content',
            field=models.TextField(blank=True, verbose_name='О существе'),
        ),
    ]
