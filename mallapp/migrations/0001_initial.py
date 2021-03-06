# Generated by Django 3.2 on 2021-04-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('firstname', models.CharField(max_length=100, verbose_name='first_name')),
                ('lastname', models.CharField(max_length=100, verbose_name='last_name')),
                ('age', models.IntegerField(verbose_name='age')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('position', models.CharField(max_length=100, verbose_name='position')),
                ('username', models.EmailField(max_length=254, verbose_name='username')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
    ]
