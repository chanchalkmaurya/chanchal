# Generated by Django 3.2 on 2023-01-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_contact_details_send_a_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletteremail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]