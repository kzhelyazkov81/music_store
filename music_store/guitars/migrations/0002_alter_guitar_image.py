# Generated by Django 4.1.3 on 2022-12-04 10:39

from django.db import migrations, models
import music_store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='image',
            field=models.FileField(upload_to='images', validators=[music_store.validators.validate_file_size]),
        ),
    ]