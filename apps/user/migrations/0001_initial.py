# Generated by Django 2.0 on 2018-01-08 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('user_guid', models.CharField(max_length=32, verbose_name='用户guid')),
                ('user_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='用户名')),
                ('real_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='真实姓名')),
                ('avatar', models.CharField(blank=True, max_length=250, null=True, verbose_name='头像')),
                ('mobile', models.CharField(blank=True, max_length=50, null=True, verbose_name='手机')),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='账户余额')),
                ('available_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='可用金额')),
                ('frozen_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='冻结金额')),
                ('all_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='累计金额')),
                ('wx_open_id', models.CharField(max_length=150, verbose_name='微信OpenID')),
                ('wx_union_id', models.CharField(blank=True, max_length=150, null=True, verbose_name='微信UnionID')),
                ('create_date', models.FloatField(blank=True, null=True, verbose_name='创建时间')),
                ('last_login_date', models.FloatField(blank=True, null=True, verbose_name='最后登录时间')),
                ('ip_address', models.CharField(blank=True, max_length=50, null=True, verbose_name='IP地址')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
                'ordering': ['-create_date'],
                'managed': False,
            },
        ),
    ]
