from django.urls import path,include
from movieapp import views

urlpatterns=[
    path('',views.home_view),
    path('addmovie/',views.add_movies,name='addmovie'),
    path('listmovie/',views.listmovie_view,name='listmovie'),
    path('signup/',views.signup_view,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logout),
]