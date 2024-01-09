from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from ninja import NinjaAPI



api = NinjaAPI()

api.add_router("/patient/", "apps.patient.api.router")
api.add_router("/scheduling/", "apps.scheduling.api.router" )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('apps.core.pages.urls')),
    path('api/', api.urls),
    # path('patient/', include('apps.patient.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns