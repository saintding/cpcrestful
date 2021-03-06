# Generated by Django 2.0.4 on 2018-04-13 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='coachinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='教练姓名')),
                ('image', models.CharField(max_length=255, verbose_name='头像')),
                ('footstep', models.CharField(blank=True, max_length=255, null=True, verbose_name='足迹')),
                ('background', models.SmallIntegerField(choices=[(1, '体育学院'), (2, '武术学校'), (3, '军警/作战部队'), (4, '保镖训练营'), (5, '武馆')], default=1)),
                ('role', models.SmallIntegerField(choices=[(1, '教练'), (2, '陪练')], default=1)),
                ('brief', models.TextField(max_length=1024, verbose_name='简介')),
            ],
            options={
                'db_table': 'coachinfo',
            },
        ),
        migrations.CreateModel(
            name='collectionclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='课程名称')),
                ('course_img', models.CharField(max_length=255, verbose_name='课程缩略图')),
                ('brief', models.TextField(max_length=320, verbose_name='课程简介')),
                ('total_scholarship', models.PositiveIntegerField(default=6000, verbose_name='总奖学金')),
                ('assistant_coach', models.PositiveIntegerField(default=8000, verbose_name='陪练费用')),
                ('period', models.PositiveIntegerField(default=365, help_text='方便计算返利时使用', verbose_name='建议学习天数')),
                ('prerequisite', models.TextField(max_length=1024, verbose_name='课程前提')),
                ('coach', models.ManyToManyField(to='martialboyzclub.coachinfo', verbose_name='教练')),
            ],
            options={
                'db_table': 'collectionclass',
            },
        ),
        migrations.CreateModel(
            name='pricecondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='建立与关联表对象之间的主键关联')),
                ('valid_period', models.SmallIntegerField(choices=[(1, '1次'), (3, '3次'), (7, '7次'), (14, '2周'), (30, '1个月'), (60, '2个月'), (90, '3个月'), (180, '6个月'), (210, '12个月'), (540, '18个月'), (720, '24个月')], verbose_name='时长')),
                ('price', models.FloatField(verbose_name='价格')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='建立与集体课或私教之间的联系')),
            ],
        ),
    ]
