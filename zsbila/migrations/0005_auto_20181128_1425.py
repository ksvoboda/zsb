# Generated by Django 2.1.3 on 2018-11-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsbila', '0004_auto_20181121_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
