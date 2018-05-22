# Generated by Django 2.0.4 on 2018-05-22 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApacheS', '0008_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dni', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateField()),
                ('date_delivery', models.DateField()),
                ('cancellation_date', models.DateField()),
                ('amount', models.FloatField()),
                ('state', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApacheS.Client')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApacheS.Department')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApacheS.Seller')),
            ],
        ),
    ]
