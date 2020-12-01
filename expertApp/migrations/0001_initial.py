# Generated by Django 3.1.3 on 2020-12-01 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pagesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('expertId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='', max_length=300)),
                ('email', models.EmailField(default='', max_length=50)),
                ('yearsInterviewedFor', models.CharField(choices=[('', 'Years of interviewing experience'), ('lessThanOne', 'Less than 1 year'), ('oneToThree', '1 - 3 years'), ('threeToFive', '3 - 5 years'), ('fiveToTen', '5 - 10 years'), ('moreThanTen', 'More than 10 years')], default='', max_length=12)),
                ('expertiseFunction', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pagesApp.function')),
            ],
        ),
    ]
