# Generated by Django 4.0.4 on 2022-12-29 06:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='practiceadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_icon', models.CharField(max_length=33)),
                ('desc_icon', tinymce.models.HTMLField()),
            ],
        ),
    ]
