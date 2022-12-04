# Generated by Django 4.1.3 on 2022-12-04 10:24

from django.db import migrations, models
import music_store.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Acoustic', 'Acoustic'), ('Electric', 'Electric'), ('Bass', 'Bass')], max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('fretboard', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=20)),
                ('strings', models.PositiveIntegerField(validators=[music_store.validators.validate_strings_number])),
                ('image', models.FileField(blank=True, null=True, upload_to='images', validators=[music_store.validators.validate_file_size])),
                ('price', models.FloatField()),
            ],
        ),
    ]
