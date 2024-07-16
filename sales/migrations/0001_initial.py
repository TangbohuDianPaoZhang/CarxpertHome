# Generated by Django 5.0.7 on 2024-07-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('brand', models.CharField(max_length=50, verbose_name='品牌')),
                ('model', models.CharField(max_length=255, verbose_name='车型')),
                ('carImg', models.CharField(max_length=255, verbose_name='车辆图片')),
                ('sales', models.IntegerField(verbose_name='销量')),
                ('price', models.CharField(max_length=50, verbose_name='价格')),
                ('rank', models.IntegerField(verbose_name='排名')),
                ('energyType', models.CharField(max_length=50, verbose_name='能源类型')),
                ('carType', models.CharField(max_length=50, verbose_name='车辆类型')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '汽车信息',
                'verbose_name_plural': '汽车信息',
                'db_table': 'car_info',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user',
            },
        ),
    ]
