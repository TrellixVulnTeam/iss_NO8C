from django.contrib import messages
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
        form = CreateForm(request.POST)  # CreateForm으로 부터 받은 데이터를 처리하기 위한 인스턴스 생성
        if form.is_valid():  # 폼 검증 메소드
            Request = form.save()  # Request 오브젝트를 form으로 부터 가져오지만, 실제로 DB반영은 하지 않는다.
            return redirect('request:list')  # url의 name을 경로대신 입력한다.
        else:
            return HttpResponseNotFound("Validation Failed")
    else:
        form = CreateForm()

    return render(request, 'request/request_create.html', {'form': form })

'''#백업
def RequestListCreate_backup(request):
    #----------------------------------------- [수정]---------------------------------------------#
    # + Create New버튼 클릭 시 GET 방식으로 호출하면서 POST 여부를 체크하니까
    # Validation Failed 발생
    # POST 방식을 사용할때 화면에서 <form method="post"... 라고 작성해야 하며,
    # 로그인, 폼 입력 후 저장할 때 POST 방식으로 전달 함
    # -------------------------------------------------------------------------------------------#
    #if request.method == "POST":
    form = CreateForm(request.POST) #CreateForm으로 부터 받은 데이터를 처리하기 위한 인스턴스 생성
    if form.is_valid():#폼 검증 메소드
        Request = form.save()#Request 오브젝트를 form으로 부터 가져오지만, 실제로 DB반영은 하지 않는다.
        Request.generate()
        return redirect('/')  # url의 name을 경로대신 입력한다.
    #else:
    #    return HttpResponseNotFound("Validation Failed")

    return render(request, 'request/request_create.html', { 'form': form })
'''



class RequsetDetailView(DetailView):
    model = Request  # 연결할 모델을 지정해 준다.

class RequestUpdateView(UpdateView):
    model = Request  # 연결할 모델을 지정해 준다.
    fields = ['subject', 'finished_date', 'memo']   #전체 필드값 중 어떤 필드값에 대해 다룰 것인지 설정. all도 가능하나 거의 사용하지 않음
    template_name_suffix = '_update'#Create와 같은 경우 장고에서 자동으로 html 파일명 뒤에 '_form'을 강제로 붙여버리므로 이를 방지하기 위해 suffix 옵션을 사용한다.

class RequestDeleteView(DeleteView):
    model = Request  # 연결할 모델을 지정해 준다.
    success_url = reverse_lazy('list')

