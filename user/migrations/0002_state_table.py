# Generated by Django 4.1.7 on 2023-12-19 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='state_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=20)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country_table')),
            ],
        ),
    ]