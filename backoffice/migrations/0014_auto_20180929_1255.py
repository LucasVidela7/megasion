# Generated by Django 2.1 on 2018-09-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0013_auto_20180928_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(upload_to='backoffice/static/images/categorias/'),
        ),
    ]