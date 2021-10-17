# Generated by Django 3.2.8 on 2021-10-17 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]),
        ),
        migrations.AlterField(
            model_name='musician',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
