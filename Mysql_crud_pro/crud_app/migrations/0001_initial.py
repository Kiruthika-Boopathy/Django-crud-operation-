# Generated by Django 4.2.4 on 2023-08-23 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rank', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
