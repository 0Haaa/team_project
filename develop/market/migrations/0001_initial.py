# Generated by Django 3.2.14 on 2022-10-07 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='물품 제목')),
                ('description', models.TextField(verbose_name='물품 설명')),
                ('item_category', models.CharField(choices=[('운동기구', '운동기구'), ('운동화', '운동화'), ('운동복', '운동복'), ('보조식품', '보조식품'), ('기타', '기타')], max_length=20, verbose_name='물품 종류')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('region', models.CharField(choices=[('동구', '동구'), ('서구', '서구'), ('남구', '남구'), ('북구', '북구'), ('광산구', '광산구')], max_length=5, verbose_name='위치')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='modify date')),
                ('img1', models.FileField(default=None, upload_to='market_item/%Y/%m/%d/', verbose_name='물품 이미지')),
                ('img2', models.FileField(default=None, upload_to='market_item/%Y/%m/%d/')),
                ('img3', models.FileField(default=None, upload_to='market_item/%Y/%m/%d/')),
                ('user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='로그인 유저')),
            ],
            options={
                'ordering': ('-modify_dt',),
            },
        ),
    ]
