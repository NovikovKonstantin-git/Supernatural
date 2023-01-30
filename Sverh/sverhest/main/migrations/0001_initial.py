# Generated by Django 3.2.7 on 2021-10-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
