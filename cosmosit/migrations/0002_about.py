# Generated by Django 3.2.6 on 2021-09-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmosit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=230)),
                ('content', models.CharField(max_length=200)),
                ('list', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'about',
                'db_table': 'about',
            },
        ),
    ]
