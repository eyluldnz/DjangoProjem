# Generated by Django 3.0.3 on 2020-03-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200328_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
