# Generated by Django 4.0 on 2022-01-07 04:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('comment', models.TextField()),
                ('at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
