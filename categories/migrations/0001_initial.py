# Generated by Django 4.0.4 on 2022-06-01 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='categories')),
                ('details', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
