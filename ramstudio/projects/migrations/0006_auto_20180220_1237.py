# Generated by Django 2.0.2 on 2018-02-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180220_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photos',
            field=models.ManyToManyField(related_name='projects', to='projects.Photo'),
        ),
    ]