# Generated by Django 2.0.2 on 2018-02-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20180220_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='+', to='projects.Photo'),
        ),
    ]