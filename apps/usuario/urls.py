from django.urls import path

from apps.usuario.views import Login, RegisterUser, index, ShowUser, DeleteUser, UpdateUser, Logout

app_name = 'usuario'

urlpatterns = [
    path('', index, name='index'),
    path('list', ShowUser.as_view(), name='list'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<int:pk>/edit_user', UpdateUser.as_view(), name='edit_user'),
    path('<int:pk>/delete_user', DeleteUser.as_view(), name='delete_user'),
]