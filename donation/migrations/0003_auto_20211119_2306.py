# Generated by Django 3.2.6 on 2021-11-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_auto_20211109_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='adminremark',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='updationdate',
            field=models.DateField(null=True),
        ),
    ]
