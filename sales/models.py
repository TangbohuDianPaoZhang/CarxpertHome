from django.db import models

# Create your models here.
class CarInfo(models.Model):
    id = models.AutoField('id', primary_key=True)
    brand = models.CharField('品牌', max_length=50)
    model = models.CharField('车型', max_length=255)
    carImg = models.CharField('车辆图片', max_length=255)
    sales = models.IntegerField('销量')
    minPrice = models.DecimalField('最低价', max_digits=10, decimal_places=2)
    maxPrice = models.DecimalField('最高价', max_digits=10, decimal_places=2)
    rank = models.IntegerField('排名')
    energyType = models.CharField('能源类型', max_length=50)
    carType = models.CharField('车辆类型', max_length=50)
    month = models.CharField('月份', max_length=50)

    class Meta:
        db_table = 'car_info'
        verbose_name = '汽车信息'
        verbose_name_plural = verbose_name


class User(models.Model):
    id = models.AutoField('id', primary_key=True)
    username = models.CharField('用户名', max_length=50)
    password = models.CharField('密码', max_length=50)
    email = models.CharField('邮箱', max_length=50)
    createTime = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
