from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'medidores', views.MedidorViewSet)
router.register(r'mediciones', views.MedicionViewSet)
router.register(r'minimoConsumo/(?P<llave>.*)',  views.minimoConsumoViewSet)
router.register(r'maximoConsumo/(?P<llave>.*)',  views.maximoConsumoViewSet)
router.register(r'consumoTotal/(?P<llave>.*)',  views.consumoTotalViewSet)
router.register(r'consumoPromedio/(?P<llave>.*)',  views.consumoPromedioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]