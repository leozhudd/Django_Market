# Generated by Django 3.0.3 on 2020-09-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20200909_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
