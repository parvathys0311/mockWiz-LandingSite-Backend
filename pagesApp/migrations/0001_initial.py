# Generated by Django 3.1.3 on 2020-12-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('functionID', models.AutoField(primary_key=True, serialize=False)),
                ('functionName', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
