from django.contrib import admin

# Register your models here.
from devpro.encurtador.models import UrlLog, UrlRedirect

@admin.register(UrlRedirect)
class UrlRedirect(admin.ModelAdmin):
    list_display = ('destino', 'slug', 'criado_em', 'atualizado_em')

@admin.register(UrlLog)
class UrlLogAdmin(admin.ModelAdmin):
    list_display = ('origem', 'criado_em', 'user_agent', 'host', 'ip', 'url_redirect')

    def has_changed_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False