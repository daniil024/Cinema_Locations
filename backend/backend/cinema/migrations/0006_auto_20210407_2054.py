# Generated by Django 3.1.5 on 2021-04-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_auto_20210405_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='photo_link',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]
