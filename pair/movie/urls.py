from django.urls import path
from . import views

# url namespace
# url을 이름으로 분류하는 기능

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
]