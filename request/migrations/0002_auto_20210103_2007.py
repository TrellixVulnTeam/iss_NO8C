# Generated by Django 3.1.4 on 2021-01-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='mail',
        ),
        migrations.AlterField(
            model_name='request',
            name='project',
            field=models.CharField(blank=True, choices=[('project_ksw_siljuck', '감사원 - 실적평가'), ('project_ykb_youjibosu', '외교부 - 전자감사'), ('default', '프로젝트를 선택해주세요'), ('project_ksw_youjibosu', '감사원 - 유지보수')], max_length=50, null=True),
        ),
    ]