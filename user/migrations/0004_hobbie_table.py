# Generated by Django 4.1.7 on 2023-12-29 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0007_rename_season_factor_seasonfactor_table'),
        ('user', '0003_register_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='hobbie_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.hobby_table')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_table')),
            ],
        ),
    ]
