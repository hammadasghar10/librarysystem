# Generated by Django 4.2.3 on 2023-07-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='All images')),
            ],
        ),
    ]