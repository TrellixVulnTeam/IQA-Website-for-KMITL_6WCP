# Generated by Django 2.0.2 on 2018-10-06 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0003_studyprogram_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyprogram',
            name='pdf_docs',
            field=models.FileField(default=django.utils.timezone.now, upload_to='study_program_details/'),
            preserve_default=False,
        ),
    ]
