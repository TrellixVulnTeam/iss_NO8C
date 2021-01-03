from django.urls import path

from . import views
from .views import *
from .forms import CreateForm

app_name = 'request'

urlpatterns = [
    #http://127.0.0.1/request/
    path('', RequestListView.as_view(), name='list'),  #앞에는 어떤주소로 오면 동작시킬거고 뒤에은 어떤 뷰를 동작시킬거야 라고 설정, .as_view()는 앞의(RequestListView)클래스뷰를 함수형 뷰로 바꿔주는 효과가 있어서 써준다. name=은 해당 url패턴의 이름이라고 보면된다.
    path('add/', views.RequestListCreate, name='add'),
    path('detail/<int:pk>/', RequsetDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', RequestUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RequestDeleteView.as_view(), name='delete'),
]