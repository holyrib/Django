# Generated by Django 2.1.1 on 2018-09-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180926_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.CharField(max_length=100),
        ),
    ]
