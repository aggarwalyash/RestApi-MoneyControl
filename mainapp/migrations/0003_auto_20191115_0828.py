# Generated by Django 2.2.5 on 2019-11-15 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20191115_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='mainapp.Wallet'),
        ),
    ]
