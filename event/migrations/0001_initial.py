# Generated by Django 3.2.19 on 2024-02-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('amount', models.TextField()),
                ('purpose', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event/images/')),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('event_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]