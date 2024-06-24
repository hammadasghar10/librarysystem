# Generated by Django 4.2.3 on 2023-07-30 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=20)),
                ('Quantity', models.PositiveBigIntegerField()),
                ('image', models.ImageField(upload_to='All images')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Book_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.booksdetails')),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.user')),
            ],
        ),
    ]
