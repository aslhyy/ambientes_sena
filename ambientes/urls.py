from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('ambientes', AmbienteViewSet)
router.register('inventario', ItemInventarioViewSet)
router.register('asignaciones', AsignacionViewSet)
router.register('horarios', HorarioAmbienteViewSet)
router.register('novedades', NovedadViewSet)

urlpatterns = router.urls
