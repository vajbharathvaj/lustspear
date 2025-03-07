# Generated by Django 5.1.6 on 2025-03-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_creator', models.BooleanField(default=False)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('profile_visibility', models.BooleanField(default=True)),
                ('subscription_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='joined_date')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
