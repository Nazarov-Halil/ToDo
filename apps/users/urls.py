from django.urls import path
from apps.users.views import login_logics, signup, logout_logics

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_logics, name='login'),
    path('logout/', logout_logics, name='logout'),
]
