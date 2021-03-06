# Generated by Django 2.1.2 on 2018-10-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computecalc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aws_sku', models.CharField(max_length=255)),
                ('aws_vCPU', models.PositiveIntegerField()),
                ('aws_ram', models.PositiveIntegerField()),
                ('aws_cost_per_hour', models.DecimalField(decimal_places=4, max_digits=8)),
                ('do_sku_equivalent', models.CharField(max_length=255)),
                ('do_cost_per_month', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
