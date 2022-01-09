# Generated by Django 3.2.9 on 2022-01-09 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nbd_app', '0008_alter_business_business_contact_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Police_Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=30)),
                ('hotline_number', models.BigIntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nbd_app.neighbourhood')),
            ],
        ),
    ]
