# Generated by Django 4.0.1 on 2022-01-31 20:33

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_telegram_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='discord_token',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True),
        ),
    ]