
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuario.api.viewset import UsuarioViewSet
from usuario_agrupamento.api.viewset import Usuario_AgrupamentoViewSet
from animais.api.viewset import AnimalViewSet
from agrupamentos.api.viewset import AgrupamentoViewSet
from historico.api.viewset import HistoricoViewSet
from historico_tipo.api.viewset import Historico_TipoViewSet
from raca.api.viewset import RacaViewSet
from imagens.api.viewset import ImagensViewSet
from rest_framework.authtoken.views import obtain_auth_token




router = routers.SimpleRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'usuarios_agrupamentos', Usuario_AgrupamentoViewSet)
router.register(r'agrupamentos', AgrupamentoViewSet)
router.register(r'animais', AnimalViewSet)
router.register(r'historicos', HistoricoViewSet)
router.register(r'historicos_tipos', Historico_TipoViewSet)
router.register(r'racas', RacaViewSet)
router.register(r'imagens', ImagensViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('rest_auth/', include('rest_auth.urls')),
    path('rest_auth/registration/', include('rest_auth.registration.urls'))
]
