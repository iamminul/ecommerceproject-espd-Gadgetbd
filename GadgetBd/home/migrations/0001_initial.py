# Generated by Django 4.0.5 on 2022-06-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_desc', models.TextField()),
                ('prod_price', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name_plural': 'Product',
            },
        ),
    ]
