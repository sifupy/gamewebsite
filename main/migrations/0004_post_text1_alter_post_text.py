# Generated by Django 4.2.7 on 2023-11-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text1',
            field=models.TextField(default='non'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
