# Generated by Django 2.1.2 on 2018-12-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemodel',
            name='id',
            field=models.CharField(default='line_2018121315194917bcad5d', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='id',
            field=models.CharField(default='route_201812131519490208e6dd', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]