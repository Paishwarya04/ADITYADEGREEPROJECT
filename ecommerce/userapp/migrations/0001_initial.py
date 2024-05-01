# Generated by Django 4.1.12 on 2024-04-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cus_name', models.CharField(max_length=100)),
                ('Cus_id', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ban_name', models.CharField(max_length=30)),
                ('Debited_A', models.IntegerField()),
                ('Credited_A', models.IntegerField()),
                ('Profit', models.IntegerField()),
            ],
        ),
    ]
