from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),

    path("account/", views.accountSettings, name="account"),
    
    path('products/', views.products, name="products"),
    path('customer/<int:pk>/', views.customer, name="customer"),

    path("create_order/<int:pk>/", views.create_order, name="create_order"),
    path("update_order/<int:pk>/", views.update_order, name="update_order"),
    path("delete_order/<int:pk>/", views.delete_order, name="delete_order"),

    path("password_reset/",
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
        name="password_reset"),

    path("password_reset_sent/",
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name="password_reset_done"),

    path("reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"),

    path("reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
        name="password_reset_complete"),
    
]


'''
1 - Submit email form                       //PasswordResetView.as_view()
2 - Email send success message              //PasswordResetDoneView.as_view()
3 - Link to password Reset form in mail     //PasswordResetConfirmView.as_view()
4 - Password successfully changed message   //PasswordResetCompleteView.as_veiw()
'''