# Generated by Django 4.0 on 2021-12-22 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=200)),
                ('insname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp', models.CharField(max_length=100)),
                ('il', models.CharField(max_length=400)),
                ('couse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp1.allcourse')),
            ],
        ),
    ]
