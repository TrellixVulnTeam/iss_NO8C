from django import forms

from account.models import Account


class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=20,  #문자수 제한하기
        required=True,  #필수항목인지
        label='ID', #라벨
        widget=forms.TextInput(attrs={  #폼타입설정(TextInput:text, TextareaInput:textarea, PasswordInput:password
            'class': 'login_form_id',
            'placeholder': 'ID'
        })
    )
    password = forms.CharField(
        max_length=20,  #문자수 제한
        required=True,  #필수항목인지
        label='PW', #라벨
        #최소값설정 : min_value=0,
        widget=forms.PasswordInput(attrs={    #폼타입설정(TextInput:text, TextareaInput:textarea, PasswordInput:password
            'class': 'password',    #'user_agent': forms.HiddenInput 읽기전용? 확인해봐야함
            'placeholder': 'PW'
        })
    )


