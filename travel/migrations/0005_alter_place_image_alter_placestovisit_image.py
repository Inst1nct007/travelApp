# Generated by Django 4.1.2 on 2022-10-26 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_remove_place_places_to_visit_alter_place_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(default='/places/landscape.jpg', upload_to='places'),
        ),
        migrations.AlterField(
            model_name='placestovisit',
            name='image',
            field=models.ImageField(default='/places/landscape.jpg', upload_to='places'),
        ),
    ]
