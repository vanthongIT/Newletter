# Generated by Django 3.1.4 on 2020-12-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('photo', models.FileField(null=True, upload_to='')),
                ('noidung', models.TextField(blank=True, null=True)),
            ],
        ),
    ]