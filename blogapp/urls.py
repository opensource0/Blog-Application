from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('addBlog/',views.addBlog,name='addBlog'),
    path('changePassword/',views.changePassword,name='changePassword'),
]
