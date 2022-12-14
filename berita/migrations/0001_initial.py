# Generated by Django 4.1.3 on 2022-12-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TBerita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.URLField(max_length=1000)),
                ('urlToImage', models.URLField(max_length=1000)),
                ('publishedAt', models.DateTimeField()),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Berita',
            },
        ),
    ]
