# Generated by Django 4.2.2 on 2023-06-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
    ]