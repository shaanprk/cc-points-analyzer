# Generated by Django 5.0.7 on 2024-11-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(unique=True)),
                ('content', models.TextField()),
                ('scraped_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
