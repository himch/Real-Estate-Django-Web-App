from django.urls import path
from .views import ProfileUpdateView, ProfileDetailView, UserRegisterView, UserLoginView, logout_view, \
    EmailConfirmationSentView, UserConfirmEmailView, EmailConfirmedView, EmailConfirmationFailedView, \
    UserPasswordChangeView, UserForgotPasswordView, UserPasswordResetConfirmView
from django.contrib.auth.decorators import login_required
# from . import views

urlpatterns = [
    path('user/edit/', login_required(ProfileUpdateView.as_view()), name='profile_edit'),
    path('user/<str:slug>/', login_required(ProfileDetailView.as_view()), name='profile_detail'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', login_required(logout_view), name='logout'),
    path('password-change/', login_required(UserPasswordChangeView.as_view()), name='password_change'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', login_required(UserPasswordResetConfirmView.as_view()), name='password_reset_confirm'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    # path('logout', views.logout, name='logout'),
    # path('dashboard', views.dashboard, name='dashboard')
]