from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic.list import ListView  #클래스형 뷰인 장고의 generic.list 모듈에서 ListView를 불러온다.
from django.views.generic.edit import CreateView, UpdateView, DeleteView #클래스형 뷰인 장고의 generic.edit 모듈에서 CreateView와 UpdateView를 불러온다.
from django.views.generic.detail import DetailView #클래스형 뷰인 장고의 generic.detail 모듈에서 DetailView를 불러온다.


from django.urls import reverse_lazy

from .forms import CreateForm
from .models import Request

# Create your views here.

class RequestListView(ListView):
    model = Request #연결할 모델을 지정해 준다.


def RequestListCreate(request):
    
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            Request = form.save()
            return redirect('/')
    else:
        return HttpResponseNotFound("Validation Faild")
    return render(request, 'request/request_create.html', { 'form': form })



class RequsetDetailView(DetailView):
    model = Request  # 연결할 모델을 지정해 준다.

class RequestUpdateView(UpdateView):
    model = Request  # 연결할 모델을 지정해 준다.
    fields = ['subject', 'finished_date', 'memo']   #전체 필드값 중 어떤 필드값에 대해 다룰 것인지 설정. all도 가능하나 거의 사용하지 않음
    template_name_suffix = '_update'#Create와 같은 경우 장고에서 자동으로 html 파일명 뒤에 '_form'을 강제로 붙여버리므로 이를 방지하기 위해 suffix 옵션을 사용한다.

class RequestDeleteView(DeleteView):
    model = Request  # 연결할 모델을 지정해 준다.
    success_url = reverse_lazy('list')

