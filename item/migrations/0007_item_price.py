# Generated by Django 4.2.6 on 2023-10-31 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_remove_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default='exit', max_digits=19),
            preserve_default=False,
        ),
    ]
