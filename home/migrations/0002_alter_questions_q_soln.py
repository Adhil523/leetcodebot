# Generated by Django 4.1.7 on 2023-10-11 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='q_soln',
            field=models.TextField(default=' '),
        ),
    ]