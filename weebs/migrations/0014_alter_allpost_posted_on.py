# Generated by Django 4.0.4 on 2022-06-05 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weebs', '0013_allpost_posted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allpost',
            name='posted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
