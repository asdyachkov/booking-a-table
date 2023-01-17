from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from main.views import SalatsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/salatslist/', SalatsAPIView.as_view())
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
