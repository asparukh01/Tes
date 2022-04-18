from django.urls import path, include, re_path

from api_v1.views import *

urlpatterns = []
accounts_urls = [
    path('', index_view, name='registration'),
    path('api_v1/resumes', ResumeView.as_view(), name='resume_api'),
    path('api_v1/resumes/<int:pk>', ResumeDetailView.as_view(), name='detail_project_api'),
    path('api_v1/auth/', include('djoser.urls')),
    re_path('api_v1/auth/', include('djoser.urls.authtoken')),
]

urlpatterns += accounts_urls 
