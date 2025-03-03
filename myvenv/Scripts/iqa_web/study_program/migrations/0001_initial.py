# Generated by Django 2.0.2 on 2018-10-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('program_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('GOING TO CLOSE', 'GOING TO CLOSE'), ('NOT ACTIVE', 'NOT ACTIVE')], max_length=200)),
                ('degree_and_major', models.CharField(max_length=400)),
                ('collaboration_with_other_institues', models.TextField(choices=[('Program issued specifically by KMITL', 'Program issued specifically by KMITL'), ('Program supported by other institutes', 'Program supported by other institutes'), ('Collaborated program with other institutes', 'Collaborated program with other institutes')], max_length=400)),
            ],
        ),
    ]
