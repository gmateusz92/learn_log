# Generated by Django 4.0.4 on 2022-04-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
