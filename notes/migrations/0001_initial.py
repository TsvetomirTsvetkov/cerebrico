# Generated by Django 5.0.2 on 2024-06-02 14:21

import django.core.validators
import django.db.models.deletion
import notes.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('upload', models.FileField(upload_to=notes.utils.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['md', 'txt'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'title')},
            },
        ),
    ]
