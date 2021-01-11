# Generated by Django 3.1.4 on 2021-01-07 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20210107_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='name',
            field=models.CharField(choices=[('', '희망 담당자'), ('name_yhj', '양현정 주임'), ('name_ksh', '강승환 팀장'), ('name_ksm', '김선민 주임'), ('name_akh', '안계훈 선임')], default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='project',
            field=models.CharField(choices=[('project_ksw_youjibosu', '감사원 - 유지보수'), ('project_ksw_siljuck', '감사원 - 실적평가'), ('project_ykb_youjibosu', '외교부 - 전자감사'), ('', '프로젝트')], default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='work_class',
            field=models.CharField(choices=[('work_plan', '기획'), ('work_development', '개발'), ('work_publishing', '퍼블리싱'), ('', '업무 분류'), ('work_design', '디자인')], default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='work_class_detail',
            field=models.CharField(choices=[('work_plan', '기획'), ('work_development', '개발'), ('work_publishing', '퍼블리싱'), ('', '업무 분류'), ('work_design', '디자인')], default='', max_length=50, null=True),
        ),
    ]