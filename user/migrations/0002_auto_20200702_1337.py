# Generated by Django 2.2.3 on 2020-07-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='bgImage',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.TextField(default=''),
        ),
    ]
