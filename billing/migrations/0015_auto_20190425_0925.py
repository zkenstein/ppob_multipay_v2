# Generated by Django 2.2 on 2019-04-25 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('witdraw', '0001_initial'),
        ('billing', '0014_commisionrecord_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='commisionrecord',
            name='is_withdraw',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='commisionrecord',
            name='withdraw',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='witdraw.Witdraw'),
        ),
    ]