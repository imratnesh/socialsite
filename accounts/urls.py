from django.contrib import admin
from django.urls import path, reverse_lazy, re_path
from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from . import views
from django.views.generic import RedirectView

app_name = 'accounts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('changePassword/', PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')),
         name='password_change'),
    path('passwordChanged/', PasswordChangeDoneView.as_view(), name='password_change_done'),



    path('resetPassword/', PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),
         name='password_reset'),
    path('passwordReset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

    re_path(r'passwordResetConfirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')),
            name='password_reset_confirm'),

    path('passwordReset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
