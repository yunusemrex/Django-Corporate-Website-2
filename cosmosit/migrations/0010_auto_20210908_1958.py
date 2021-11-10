# Generated by Django 3.2.6 on 2021-09-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmosit', '0009_remove_hero_h_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='icons')),
            ],
        ),
        migrations.RemoveField(
            model_name='features',
            name='ficon',
        ),
    ]
