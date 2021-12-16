# Generated by Django 3.2.9 on 2021-12-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20211214_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstore',
            name='logo',
            field=models.TextField(default='stores/logos/no-logo.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(default='stores/logos/no-logo.png', upload_to='stores/logos'),
        ),
    ]
