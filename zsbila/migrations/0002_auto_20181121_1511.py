# Generated by Django 2.1.3 on 2018-11-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsbila', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kontakty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=200, verbose_name='Jmeno')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('tridni', models.CharField(max_length=200, verbose_name='Třídní')),
                ('predmety', models.CharField(max_length=200, verbose_name='Předměty')),
            ],
            options={
                'verbose_name': 'kontakt',
                'verbose_name_plural': 'kontakty',
            },
        ),
        migrations.DeleteModel(
            name='GalleryPic',
        ),
        migrations.RemoveField(
            model_name='pageblock',
            name='block_page',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='item_internal',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='PageBlock',
        ),
    ]
