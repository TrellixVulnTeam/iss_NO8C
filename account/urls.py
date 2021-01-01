from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
import account.views
from . import views

from account import views
from account.views import AccountCreateView

app_name = 'account'

urlpatterns = [

    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),   #로그인은 템플릿을 따로 설정해준다.
    path('logout/', LogoutView.as_view(), name='logout'), #사용자가 입력했을 때 경로를 넣고,   views.py에서 설정한 클래스뷰 명칭을 넣고 함수형이 아닌 클래스형 뷰(장고제공뷰)이기 때문에 뒤에 .as_view()를 꼭 넣어준다. 뒤에는 name은 html에서 받을 이름임
    path('create/', AccountCreateView.as_view(), name='create'),
]