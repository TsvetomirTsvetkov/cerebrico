# Generated by Django 5.0.2 on 2024-06-02 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('CB', 'CheckButton')], default='CB')),
                ('keyword', models.CharField(max_length=50)),
                ('separator', models.CharField(max_length=2)),
                ('is_prefix', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile Settings',
                'unique_together': {('user', 'keyword', 'separator', 'is_prefix')},
            },
        ),
    ]
