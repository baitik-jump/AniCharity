from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('about_us', views.abouUS),
    path('tops', views.tops),
    path('forum', views.forum),

]
# body {
# background: #c7b39b url({% static 'main/img/background.jpg' %});
#
# }