# Generated by Django 4.1.2 on 2022-11-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_alter_place_image_alter_placestovisit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='price',
            field=models.BigIntegerField(null=True),
        ),
    ]