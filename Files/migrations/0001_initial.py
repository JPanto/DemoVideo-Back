# Generated by Django 3.0.12 on 2021-02-19 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=100)),
                ('path', models.FileField(upload_to='files/', verbose_name='')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Files.TypeFile')),
            ],
        ),
    ]
