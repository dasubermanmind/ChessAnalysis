"""chessController URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiv1.urls')),
    path('', include('apiv1.urls'))
]
