# Generated by Django 2.2 on 2021-02-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field=433, null=True, upload_to='', width_field=640),
        ),
    ]
