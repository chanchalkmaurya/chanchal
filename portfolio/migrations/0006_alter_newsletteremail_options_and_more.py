# Generated by Django 4.1.5 on 2023-05-09 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_details'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletteremail',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='project_details',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='send_a_query',
            options={'ordering': ['-id']},
        ),
    ]
