# Generated by Django 4.0 on 2024-04-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login_std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='signup_std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('contact', models.IntegerField()),
                ('dob', models.DateField()),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
