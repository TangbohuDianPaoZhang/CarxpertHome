# Generated by Django 5.0.7 on 2024-07-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carinfo',
            name='price',
        ),
        migrations.AddField(
            model_name='carinfo',
            name='maxPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='最高价'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carinfo',
            name='minPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='最低价'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carinfo',
            name='month',
            field=models.CharField(default=202305, max_length=50, verbose_name='月份'),
            preserve_default=False,
        ),
    ]