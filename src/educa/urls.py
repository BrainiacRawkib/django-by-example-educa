from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from courses.views import CourseListView

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(extra_context={'title': 'Login'}),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('', CourseListView.as_view(), name='course_list'),
]

admin.site.site_header = 'Educa Project'
admin.site.site_title = 'Educa Project'
admin.site.index_title = 'Welcome Onboard!'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
