# Generated by Django 3.2.10 on 2022-02-01 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perso', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suvu',
            fields=[
                ('suvuhale', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='связка')),
                ('perehale', models.ForeignKey(db_column='perehale', on_delete=django.db.models.deletion.CASCADE, related_name='yuvadeye', to='perso.pere', verbose_name='персона')),
                ('zovohalebe', models.ForeignKey(db_column='zovohalebe', on_delete=django.db.models.deletion.CASCADE, related_name='puyasesu', to='order.zovo', verbose_name='зазаявка')),
                ('zovohalepe', models.ForeignKey(db_column='zovohalepe', on_delete=django.db.models.deletion.CASCADE, related_name='hepapano', to='order.zovo', verbose_name='отзаявка')),
            ],
        ),
    ]