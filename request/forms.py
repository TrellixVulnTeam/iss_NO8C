from django import forms

from .models import Request


class CreateForm(forms.ModelForm):

  class Meta:
    model = Request
    fields = [
        'subject',
        'project',
        'name',
        'finished_date',
        'work_class',
        'work_class_detail',
        'memo',
    ]


    widgets = {
        'subject': forms.TextInput(
            attrs={
                'placeholder': '제목을 입력해 주세요'
            }
        ),
        'project': forms.Select(
            attrs={
                'placeholder': '제목을 입력해 주세요'
            }
        ),
        'name': forms.Select(
            attrs={
            }
        ),
        'finished_date': forms.TextInput(
            attrs={
                'id': 'Datepicker',
                'placeholder': '완료 요청일'
            }
        ),
        'work_class': forms.Select(
            attrs={
            }
        ),
        'work_class_detail': forms.Select(
            attrs={
            }
        ),
        'memo': forms.Textarea(
            attrs={
                'style': 'min-height:300px',
                'placeholder': '상세 요청 내용을 입력해 주세요'
            }
        ),
    }
