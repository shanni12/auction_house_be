# Generated by Django 3.0.5 on 2020-04-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('starting_bid', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=15)),
                ('deadline', models.DateField(max_length=20, null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('bids', models.TextField(default='{}')),
                ('uploaded_by', models.CharField(max_length=20)),
            ],
        ),
    ]
