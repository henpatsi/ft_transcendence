# Generated by Django 5.1.4 on 2024-12-18 20:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('loser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loser', to='account.account')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winner', to='account.account')),
            ],
        ),
    ]
