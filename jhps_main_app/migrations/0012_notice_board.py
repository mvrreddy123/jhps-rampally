# Generated by Django 4.1.4 on 2023-03-06 09:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jhps_main_app', '0011_delete_notice_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice_Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
                ('date', models.DateField()),
            ],
        ),
    ]