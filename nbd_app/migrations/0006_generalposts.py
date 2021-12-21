# Generated by Django 3.2.9 on 2021-12-21 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nbd_app', '0005_business'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nbd_app.neighbourhood')),
            ],
        ),
    ]
