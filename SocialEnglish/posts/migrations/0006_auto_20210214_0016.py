# Generated by Django 2.2 on 2021-02-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, height_field=433, upload_to='', width_field=640),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.TextField(default='emptyslug', unique=True),
        ),
    ]