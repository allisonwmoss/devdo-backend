# Generated by Django 3.2.8 on 2021-10-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devdo', '0003_auto_20211019_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='user_story',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
