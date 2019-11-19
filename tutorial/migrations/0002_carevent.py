# Generated by Django 2.2.7 on 2019-11-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarEvent',
            fields=[
                ('ordNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('carNumber', models.CharField(max_length=16)),
                ('trainIndex', models.CharField(blank=True, max_length=16, null=True)),
                ('trainNumber', models.CharField(blank=True, max_length=16, null=True)),
                ('carStatus', models.CharField(blank=True, max_length=64)),
                ('invoiceId', models.CharField(max_length=16)),
                ('invoiceNumber', models.CharField(max_length=16)),
                ('stateId', models.IntegerField()),
                ('lastOperDt', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]