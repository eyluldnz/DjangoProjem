# Generated by Django 3.0.3 on 2020-06-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(max_length=255),
        ),
    ]
