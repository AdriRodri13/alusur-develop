"""
URL configuration for Alusur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import ServicioSitemap, ProyectoFinalizadoSitemap, StaticViewSitemap, EntradaBlogSitemap
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

sitemaps = {
    'static': StaticViewSitemap,
    'servicios': ServicioSitemap,
    'proyectos': ProyectoFinalizadoSitemap,
    'blog': EntradaBlogSitemap,
    # 'presentacion': TextoPresentacionSitemap,  # Descomenta si tienes URLs individuales
}

# URLs sin prefijo de idioma (para admin, sitemap, cambio de idioma)
urlpatterns = [
    path('django-admin/', admin.site.urls),
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('i18n/setlang/', set_language, name='set_language'),  # Cambio de idioma
]

# URLs con prefijo de idioma (/es/, /en/)
urlpatterns += i18n_patterns(
    path("", include("app.urls")),
    prefix_default_language=True  # Incluir /es/ para español también
)
