# Generated by Django 2.2.6 on 2020-03-22 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_issuedbooks_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedHistorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
