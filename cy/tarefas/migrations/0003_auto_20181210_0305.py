# Generated by Django 2.0.6 on 2018-12-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0002_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='entrada',
            field=models.CharField(max_length=250),
        ),
    ]