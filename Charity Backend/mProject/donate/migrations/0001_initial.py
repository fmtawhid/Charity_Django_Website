# Generated by Django 4.2.2 on 2023-06-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donarList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=11)),
            ],
        ),
    ]