# Generated by Django 3.2.7 on 2021-10-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='cover_letter',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
