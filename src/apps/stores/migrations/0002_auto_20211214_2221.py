# Generated by Django 3.2.9 on 2021-12-14 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstore',
            name='logo',
            field=models.TextField(blank=True, default='stores/logos/no-logo.png', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(blank=True, default='stores/logos/no-logo.png', null=True, upload_to='stores/logos'),
        ),
    ]