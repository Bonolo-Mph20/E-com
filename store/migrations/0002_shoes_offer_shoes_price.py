# Generated by Django 5.1.3 on 2024-11-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shoes',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
