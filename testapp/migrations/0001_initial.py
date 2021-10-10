# Generated by Django 3.2.8 on 2021-10-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=None)),
            ],
        ),
    ]
