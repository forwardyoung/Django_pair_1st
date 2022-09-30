from django.shortcuts import render, redirect
from .models import Review


# Create your views here.
def index(request):
    review_ = Review.objects.all()
    context = {
        "review": review_,
    }
    return render(
        request, "movie/index.html", context
    )
    

def new(request):
    return render(request, 'movie/new.html')

def edit(request):
    return render(request, 'movie/edit.html')

def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    # 템플릿에서 데이터를 get
    
    # content필드는 default 값이 정해져있지 않으므로 content값을 넣는다.
    Review.objects.create(title=title, content=content)
    
    # context를 create한 후 return할 때 인자로 불러와도 되긴 하나 redirect로 해보자
    return redirect("movie:index")  # runserver하면 루트 주소로 뜬다.
    # 주소창에 naver를 navet로 입력해도 naver로 연결하는 역할
