# Generated by Django 4.2.7 on 2023-11-19 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_login_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Tickets_Price', models.CharField(max_length=10)),
                ('Total_Ticket', models.CharField(max_length=50)),
                ('Event_Date', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
    ]
