# Generated by Django 5.1.4 on 2025-01-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default='password', max_length=50),
            preserve_default=False,
        ),
    ]
