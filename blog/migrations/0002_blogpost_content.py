# Generated by Django 2.2.6 on 2019-10-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
