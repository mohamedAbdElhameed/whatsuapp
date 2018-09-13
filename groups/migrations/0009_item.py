# Generated by Django 2.1 on 2018-09-05 15:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_link_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_photo', models.ImageField(blank=True, null=True, upload_to='groups/')),
                ('big_title', models.CharField(max_length=200)),
                ('small_title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('about_photo', models.ImageField(blank=True, null=True, upload_to='groups/')),
                ('about_title', models.CharField(blank=True, max_length=100, null=True)),
                ('about_version', models.CharField(blank=True, max_length=100, null=True)),
                ('about_sub_title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]