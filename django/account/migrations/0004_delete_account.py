# Generated by Django 5.1.4 on 2025-01-02 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_username'),
        ('match_history', '0003_alter_match_loser_alter_match_winner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]