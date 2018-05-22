# Generated by Django 2.0.4 on 2018-05-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApacheS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('company', models.CharField(default='', max_length=50)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]