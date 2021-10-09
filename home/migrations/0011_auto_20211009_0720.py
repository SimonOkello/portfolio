# Generated by Django 3.2.7 on 2021-10-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_skill_skill_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='c_vitae',
            field=models.FileField(upload_to='media/CVS/%Y/%m/%D'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='cover_letter',
            field=models.FileField(blank=True, null=True, upload_to='media/CoverLetters/%Y/%m/%D'),
        ),
    ]