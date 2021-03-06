# Generated by Django 2.1 on 2018-10-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0017_auto_20181002_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='model_pic',
            new_name='foto_producto_2',
        ),
        migrations.AddField(
            model_name='producto',
            name='foto_producto_1',
            field=models.ImageField(default=-3.0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='foto_producto_3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='foto_producto_4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='foto_producto_5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
