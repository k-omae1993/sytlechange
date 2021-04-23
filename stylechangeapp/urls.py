from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.top, name='top'),
  path('index/', views.index, name='index'),
  path('login/', views.Login.as_view(), name='login'), # 追加
  path('logout/', views.Logout.as_view(), name='logout'), 
  path('test/', views.test, name='test'),
  path('signup/', views.SignUp.as_view(), name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)