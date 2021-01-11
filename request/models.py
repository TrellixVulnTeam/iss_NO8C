from django.db import models
from django.urls import reverse

"""""""""""
★ 필드옵션 : 필드마다 고유 옵션이 존재, 공통 적용 옵션도 있음
null (DB 옵션) : DB 필드에 NULL 허용 여부 (디폴트 : False)
unique (DB 옵션) : 유일성 여부 (디폴트 : False)
blank : 입력값 유효성 (validation) 검사 시에 empty 값 허용 여부 (디폴트 : False)
default : 디폴트 값 지정. 값이 지정되지 않았을 때 사용
verbose_name : 필드 레이블. 지정되지 않으면 필드명이 쓰여짐
validators : 입력값 유효성 검사를 수행할 함수를 다수 지정
각 필드마다 고유한 validators 들이 이미 등록되어있기도 함
예 : 이메일만 받기, 최대길이 제한, 최소길이 제한, 최대값 제한, 최소값 제한 등
choices (form widget 용) : select box 소스로 사용
help_text (form widget 용) : 필드 입력 도움말
auto_now_add : Bool, True 인 경우, 레코드 생성시 현재 시간으로 자동 저장
"""""""""""

"""""""""""
★ 필드타입
CharField : 문자열. max_length 설정이 가능하다
TextField
ImageField : 이미지
DateField : 날짜/시간
BooleanField, NullBooleanField : 참/거짓
IntegerField : 숫자
BinaryField, FileField : 파일
EmailField : 이메일
URLField : 링크
"""""""""""

# Create your models here.

class Request(models.Model):
    DEFAULTTEXT = ''

    PROJECT_CHOICES = {
        (DEFAULTTEXT, '프로젝트'),
        ('project_ksw_youjibosu', '감사원 - 유지보수'),
        ('project_ksw_siljuck', '감사원 - 실적평가'),
        ('project_ykb_youjibosu', '외교부 - 전자감사')
    }

    NAME_CHOICES = {
        (DEFAULTTEXT, '희망 담당자'),
        ('양현정 주임', '양현정 주임'),
        ('안계훈 선임', '안계훈 선임'),
        ('강승환 팀장', '강승환 팀장'),
        ('김선민 주임', '김선민 주임')
    }

    WORK_CHOICES = {
        (DEFAULTTEXT, '업무 분류'),
        ('work_plan', '기획'),
        ('work_design', '디자인'),
        ('work_publishing', '퍼블리싱'),
        ('work_development', '개발')
    }

    WORKDETAIL_CHOICES = {
        (DEFAULTTEXT, '업무 분류'),
        ('work_plan', '기획'),
        ('work_design', '디자인'),
        ('work_publishing', '퍼블리싱'),
        ('work_development', '개발')
    }


    subject = models.CharField(max_length=50, blank=False, null=False)   #제목
    project = models.CharField(max_length=50, blank=True, null=True, choices=PROJECT_CHOICES, default=DEFAULTTEXT)  #프로젝트명
    name = models.CharField(max_length=50, blank=True, null=True, choices=NAME_CHOICES, default=DEFAULTTEXT)  #담당자
    created_date = models.CharField(max_length=50, null=True, blank=True)  #신청일
    finished_date = models.CharField(max_length=50, null=True, blank=True) #완료요청일
    memo = models.TextField(max_length=2000, blank=False, null=False) #상세요청사항
    hits = models.IntegerField(null=True, blank=True)   #조회수`
    work_class = models.CharField(max_length=50, blank=True, null=True, choices=WORK_CHOICES, default=DEFAULTTEXT)    #업무분류
    work_class_detail = models.CharField(max_length=50, blank=True, null=True, choices=WORKDETAIL_CHOICES, default=DEFAULTTEXT) #업무분류상세


    def __str__(self):
        return "제목 : " + str(self.subject) + ", 프로젝트 : " + str(self.project) + ", 담당자 : " + str(self.name) + ", 신청일 : " + str(self.created_date) + ", 완료요청일 : " + str(self.finished_date) + ", 상세요청사항 : " + str(self.memo) + ", 조회수 : " + str(self.hits) + ", 업무분류 : " + str(self.work_class) + ", 업무분류상세 : " + str(self.work_class_detail)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])   #현재 글번호(id)값에 해당하는 detail 페이지로 이동




