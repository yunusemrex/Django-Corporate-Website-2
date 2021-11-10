# Generated by Django 3.2.6 on 2021-09-08 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cosmosit', '0004_auto_20210908_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='header',
            field=models.CharField(default=django.utils.timezone.now, max_length=230),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='section-images'),
            preserve_default=False,
        ),
    ]
