# Generated by Django 4.0 on 2022-06-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_id_alter_posttag_id_alter_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]