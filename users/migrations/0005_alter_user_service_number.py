# Generated by Django 4.2.13 on 2024-05-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_password_alter_user_service_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='service_number',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
