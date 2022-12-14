# Generated by Django 4.1.3 on 2022-12-06 12:58

from django.db import migrations, models
import music_store.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(help_text='Contact phone number', max_length=15, validators=[music_store.validators.validate_phone_number])),
            ],
        ),
    ]
