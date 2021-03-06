# Generated by Django 3.0.8 on 2020-12-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_auto_20201221_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('EMI', 'EMI'), ('ONLINE', 'Online')], default='', max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderitems',
        ),
        migrations.AddField(
            model_name='order',
            name='orderitems',
            field=models.ManyToManyField(to='posts.Cart'),
        ),
    ]
