# Generated by Django 4.1.3 on 2022-12-04 18:12

from django.db import migrations, models
import music_store.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrumSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('bass', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=50)),
                ('first_tom', models.CharField(blank=True, max_length=50, null=True)),
                ('second_tom', models.CharField(blank=True, max_length=50, null=True)),
                ('third_tom', models.CharField(blank=True, max_length=50, null=True)),
                ('body_material', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images', validators=[music_store.validators.validate_file_size])),
                ('price', models.FloatField()),
            ],
        ),
    ]
