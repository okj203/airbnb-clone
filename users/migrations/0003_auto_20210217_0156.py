# Generated by Django 2.2.5 on 2021-02-17 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201119_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW')], default='usd', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('kr', 'Korean')], default='en', max_length=2),
        ),
    ]
