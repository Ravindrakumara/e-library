
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from Book_API.views import current_user, UserList
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Book_API.urls')),
    path('auth_token/', obtain_jwt_token),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

