# Generated by Django 4.1.7 on 2024-01-08 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_message_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='trash_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('msgid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgid', to='user.message_table')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to='user.register_table')),
            ],
        ),
    ]
