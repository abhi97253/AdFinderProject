# Generated by Django 3.2 on 2022-07-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_advert_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
