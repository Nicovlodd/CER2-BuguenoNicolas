from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Entidad, Comunicado, EntidadAdmin
# Register your models here.

admin.site.register(Entidad)

admin.site.register(EntidadAdmin)
admin.site.register(Permission)

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'visible')
    list_filter = ('tipo', 'fecha_publicacion', 'visible')
    search_fields = ('titulo', 'detalle')
    date_hierarchy = 'fecha_publicacion'

