# Generated by Django 4.1.3 on 2022-12-05 09:17

from django.db import migrations, models
import music_store.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Microphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Vocal', 'Vocal'), ('Instrumental', 'Instrumental')], max_length=50)),
                ('frequency', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images', validators=[music_store.validators.validate_file_size])),
                ('price', models.FloatField()),
            ],
        ),
    ]