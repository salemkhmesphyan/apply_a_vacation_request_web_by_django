# Generated by Django 2.2.24 on 2022-02-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpag', '0002_auto_20220224_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='reqi_holy',
            name='see',
            field=models.CharField(default='0', max_length=1),
        ),
    ]