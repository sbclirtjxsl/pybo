

from django.urls import path

from . import views

app_name ='pybo'

urlpatterns = [
    path('a01index/', views.a01index, name='a01index'),  # a01_index 페이지 경로
    path('a02data/', views.a02data, name='a02data'),  # a02_data 페이지 경로
    path('a03notice/', views.a03notice, name='a03notice'),  # a03_notice 페이지 경로
    path('a04CF/', views.a04CF, name='a04CF'),  # a04_CF 페이지 경로
    path('a05intro/', views.a05intro, name='a05intro'),  # a05_intro 페이지 경로
    path('a06law/', views.a06law, name='a06law'),  # a06_law 페이지 경로
    path('a07search/', views.a07search, name='a07search'),  # a07_search 페이지 경로
    path('a08login/', views.a08login, name='a08login'),  # a08_login 페이지 경로

    path('', views.a01index, name='pybo_index'),  # 기본 경로를 a01_index로 설정 (pybo/로 접속 시)
    path('pybo/a01index/', views.a01index, name='a01index'),  # a01_index 페이지 경로
    path('pybo/a02data/', views.a02data, name='a02data'),  # a02_data 페이지 경로
    path('pybo/a03notice/', views.a03notice, name='a03notice'),  # a03_notice 페이지 경로
    path('pybo/a04CF/', views.a04CF, name='a04CF'),  # a04_CF 페이지 경로
    path('pybo/a05intro/', views.a05intro, name='a05intro'),  # a05_intro 페이지 경로
    path('pybo/a06law/', views.a06law, name='a06law'),  # a06_law 페이지 경로
    path('pybo/a07search/', views.a07search, name='a07search'),  # a07_search 페이지 경로
    path('pybo/a08login/', views.a08login, name='a08login'),  # a08_login 페이지 경로

    # path('', views.a01index, name='pybo_index'),  # 기본 경로를 a01_index로 설정 (pybo/로 접속 시)
]




    # path('a01_index/', views.a01_index, name='a01_index'),  # a01_index 페이지
    # path('pybo/a01_index/', views.a01_index, name='a01_index'),  # a01_index 페이지
    # path('pybo/a02_data/', views.a02_data, name='a02_data'),  # a02_data 페이지
    # path('pybo/a03_notice/', views.a03_notice, name='a03_notice'),  # a03_notice 페이지
    # path('pybo/a04_CF/', views.a04_CF, name='a04_CF'),  # a04_CF 페이지
    # path('pybo/a05_intro/', views.a05_intro, name='a05_intro'),  # a05_intro 페이지
    # path('pybo/a06_law/', views.a06_law, name='a06_law'),  # a06_law 페이지
    # path('pybo/a07_search/', views.a07_search, name='a07_search'),  # a07_search 페이지
    # path('pybo/a08_login/', views.a08_login, name='a08_login'),  # a08_login 페이지
    #

    # path('pybo/login/', views.login, name='login'),

    # path('index/', views.index, name='index'),
    # path('DATA/', views.DATA, name='DATA'),
    # path('introduction/', views.introduction, name='introduction'),
    # path('login/', views.login, name='login'),
    # path('notice/', views.notice, name='notice'),
    # path('search/', views.search, name='search'),
    # path('upper/', views.upper, name='upper'),
    # path('uhreff/', views.uhreff, name='uhreff'),

    # path('', views.home, name='home'),
    # path('pybo/DATA/', views.DATA, name='DATA'),
    # path('pybo/introduction/', views.introduction, name='introduction'),
    # path('pybo/login/', views.login, name='login'),
    # path('pybo/notice/', views.notice, name='notice'),
    # path('pybo/search/', views.search, name='search'),
    # path('pybo/upper/', views.upper, name='upper'),
#    path('', views.index, name='index'),


# view. xxxx는 views.py에 있는
# def upper(request):
#     return render(request, 'upper.html')
#여기에서 함수 이름이야 즉 views.py에 있는 함수 xxxx를 실행 시켜라
