# Generated by Django 2.1.5 on 2019-02-12 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0009_auto_20190212_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrecord',
            name='payform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.LoanRecord'),
        ),
    ]
