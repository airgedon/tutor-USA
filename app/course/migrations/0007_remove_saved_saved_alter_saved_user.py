# Generated by Django 4.0 on 2022-05-26 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_name'),
        ('course', '0006_delete_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saved',
            name='saved',
        ),
        migrations.AlterField(
            model_name='saved',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='account.user'),
        ),
    ]