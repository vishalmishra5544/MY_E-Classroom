# Generated by Django 3.1.7 on 2021-04-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0025_auto_20201012_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='question_number',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='standard',
            name='total_marks',
            field=models.PositiveIntegerField(default=20),
        ),
    ]