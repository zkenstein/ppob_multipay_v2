# Generated by Django 2.1.5 on 2019-02-18 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20190211_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseInSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('delete_on', models.DateTimeField(blank=True, null=True)),
                ('kode_produk', models.CharField(blank=True, max_length=100)),
                ('waktu', models.CharField(blank=True, max_length=100)),
                ('no_hp', models.CharField(blank=True, max_length=100)),
                ('sn', models.CharField(blank=True, max_length=100)),
                ('nominal', models.PositiveIntegerField(default=0)),
                ('ref1', models.CharField(blank=True, max_length=100)),
                ('ref2', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('ket', models.CharField(blank=True, max_length=100)),
                ('saldo_terpotong', models.PositiveIntegerField(default=0)),
                ('sisa_saldo', models.PositiveIntegerField(default=0)),
                ('sale', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transaction.InstanSale')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='ResponsePpobSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('delete_on', models.DateTimeField(blank=True, null=True)),
                ('kode_produk', models.CharField(blank=True, max_length=100)),
                ('waktu', models.CharField(blank=True, max_length=100)),
                ('idpel1', models.CharField(blank=True, max_length=100)),
                ('idpel2', models.CharField(blank=True, max_length=100)),
                ('idpel3', models.CharField(blank=True, max_length=100)),
                ('nama_pelanggan', models.CharField(blank=True, max_length=100)),
                ('periode', models.CharField(blank=True, max_length=100)),
                ('nominal', models.PositiveIntegerField(default=0)),
                ('admin', models.PositiveIntegerField(default=0)),
                ('ref1', models.CharField(blank=True, max_length=100)),
                ('ref2', models.CharField(blank=True, max_length=100)),
                ('ref3', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('ket', models.CharField(blank=True, max_length=100)),
                ('saldo_terpotong', models.PositiveIntegerField(default=0)),
                ('sisa_saldo', models.PositiveIntegerField(default=0)),
                ('url_struk', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='ppobsale',
            name='inquery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ppob_inquery', to='transaction.PpobSale'),
        ),
        migrations.AddField(
            model_name='responseppobsale',
            name='sale',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transaction.PpobSale'),
        ),
    ]
