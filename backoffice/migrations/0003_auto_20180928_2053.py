# Generated by Django 2.1 on 2018-09-28 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0002_auto_20180928_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorias',
            old_name='category_name',
            new_name='nombre_categoria',
        ),
    ]
