# Generated by Django 4.1.3 on 2022-11-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contectTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField(max_length=10)),
            ],
        ),
    ]