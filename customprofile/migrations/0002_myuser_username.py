# Generated by Django 5.0.1 on 2024-02-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='exit', max_length=90),
            preserve_default=False,
        ),
    ]
