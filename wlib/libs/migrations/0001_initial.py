# Generated by Django 4.2 on 2023-04-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publish_year', models.DateField()),
                ('status', models.CharField(choices=[('NS', 'Not started'), ('IP', 'In progress'), ('DN', 'Done')], default='NS', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('developer', models.CharField(max_length=50)),
                ('hours_played', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('director', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('NV', 'Not viewed'), ('V', 'Viewed')], default='NV', max_length=2)),
            ],
        ),
    ]
