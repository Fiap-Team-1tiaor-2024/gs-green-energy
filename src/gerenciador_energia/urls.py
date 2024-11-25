
from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import routers
from core.views import dashboard
from core.views_api import FonteEnergiaViewSet, TarifaEnergiaViewSet, ConsumoViewSet, HabitatViewSet


router = routers.DefaultRouter()
router.register(r'fontes', FonteEnergiaViewSet)
router.register(r'tarifas', TarifaEnergiaViewSet)
router.register(r'consumos', ConsumoViewSet)
router.register(r'habitats', HabitatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]