# Generated by Django 2.2.5 on 2019-11-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20191115_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='action',
            field=models.CharField(choices=[('1', 'Added'), ('2', 'Spent')], max_length=1),
        ),
    ]