# Generated by Django 2.0.4 on 2018-05-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApacheS', '0002_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('typeproducts', models.CharField(default='', max_length=50)),
            ],
        ),
    ]