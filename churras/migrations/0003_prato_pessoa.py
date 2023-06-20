# Generated by Django 4.2.2 on 2023-06-20 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('churras', '0002_alter_prato_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='pessoa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
    ]
