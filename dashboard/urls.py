from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    dashboard,
    profile,
    profile_edit,
    messages,
    messages_api,
    projects,
    projects_api
    )

app_name = 'dashboard'
urlpatterns = [

    path('', dashboard, name='dashboard'),

    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),

    path('messages', messages, name='messages'),
    path('messages/api/', messages_api, name='messages_api'),

    path('projects', projects, name='projects'),
    path('projects/api/', projects_api, name='projects_api'),

    path('logout/', LogoutView.as_view(), name='logout')
]
