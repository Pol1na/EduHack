from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('school/', include('myschool.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

