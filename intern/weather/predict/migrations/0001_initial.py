# Generated by Django 4.1.1 on 2022-09-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=90)),
            ],
        ),
    ]