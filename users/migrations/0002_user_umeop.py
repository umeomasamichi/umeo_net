# Generated by Django 3.1.4 on 2020-12-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='umeop',
            field=models.IntegerField(blank=True, default=0, verbose_name='Umeo Point'),
        ),
    ]