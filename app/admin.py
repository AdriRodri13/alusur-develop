from django.contrib import admin
from .models import Servicio, ProyectoFinalizado, TextoPresentacion, Parrafo, EntradaBlog


class ParrafoServicioInline(admin.TabularInline):
    model = Parrafo
    fk_name = "servicio"
    extra = 1
    fields = ("titulo", "contenido", "titulo_en", "contenido_en", "imagen")


class ParrafoProyectoInline(admin.TabularInline):
    model = Parrafo
    fk_name = "proyecto"
    extra = 1
    fields = ("titulo", "contenido", "titulo_en", "contenido_en", "imagen")

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "titulo_en")
    search_fields = ("titulo", "titulo_en", "descripcion", "descripcion_en")
    list_per_page = 25
    inlines = [ParrafoServicioInline]
    
    fieldsets = (
        ('Contenido en Español', {
            'fields': ('titulo', 'descripcion', 'imagen')
        }),
        ('Contenido en Inglés (English)', {
            'fields': ('titulo_en', 'descripcion_en'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ProyectoFinalizado)
class ProyectoFinalizadoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "titulo_en")
    search_fields = ("titulo", "titulo_en", "descripcion", "descripcion_en")
    list_per_page = 25
    inlines = [ParrafoProyectoInline]
    
    fieldsets = (
        ('Contenido en Español', {
            'fields': ('titulo', 'descripcion', 'imagen')
        }),
        ('Contenido en Inglés (English)', {
            'fields': ('titulo_en', 'descripcion_en'),
            'classes': ('collapse',)
        }),
    )

@admin.register(TextoPresentacion)
class TextoPresentacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "titulo_en")
    search_fields = ("titulo", "titulo_en", "descripcion", "descripcion_en")
    list_per_page = 25
    
    fieldsets = (
        ('Contenido en Español', {
            'fields': ('titulo', 'descripcion', 'imagen')
        }),
        ('Contenido en Inglés (English)', {
            'fields': ('titulo_en', 'descripcion_en'),
            'classes': ('collapse',)
        }),
    )


@admin.register(EntradaBlog)
class EntradaBlogAdmin(admin.ModelAdmin):
    list_display = ("titulo", "titulo_en", "publicado", "fecha_creacion")
    search_fields = ("titulo", "titulo_en", "descripcion", "descripcion_en")
    list_filter = ("publicado", "fecha_creacion")
    list_per_page = 25
    prepopulated_fields = {"slug": ("titulo",)}
    
    fieldsets = (
        ('Contenido en Español', {
            'fields': ('titulo', 'descripcion', 'imagen_portada', 'slug', 'publicado')
        }),
        ('Contenido en Inglés (English)', {
            'fields': ('titulo_en', 'descripcion_en'),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')


@admin.register(Parrafo)
class ParrafoAdmin(admin.ModelAdmin):
    list_display = ("id", "servicio", "proyecto", "entrada_blog", "titulo")
    list_filter = ("servicio", "proyecto", "entrada_blog")
    search_fields = ("titulo", "titulo_en", "contenido", "contenido_en")
    list_per_page = 25
    
    fieldsets = (
        ('Relación', {
            'fields': ('servicio', 'proyecto', 'entrada_blog')
        }),
        ('Contenido en Español', {
            'fields': ('titulo', 'contenido', 'imagen')
        }),
        ('Contenido en Inglés (English)', {
            'fields': ('titulo_en', 'contenido_en'),
            'classes': ('collapse',)
        }),
    )
