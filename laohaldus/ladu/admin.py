from django.contrib import admin
from .models import Toode, Tootekategooria
from django.utils.html import format_html

@admin.register(Toode)
class ToodeAdmin(admin.ModelAdmin):
    list_display = ('nimi', 'partii_number', 'kogus', 'aegumiskuupaev')
    search_fields = ('nimi', 'partii_number')
    list_filter = ('aegumiskuupaev',)

def qr_kood_thumbnail(self, obj):
    if obj.qr_kood:
        return format_html('<img src="{}" width="50" height="50" />', obj.qr_kood.url)
    return "-"

qr_kood_thumbnail.short_description = "QR-kood"

def pilt_thumbnail(self, obj):
    if obj.pilt:
        return format_html('<img src="{}" width="50" height="50" />', obj.pilt.url)
    return "-"

pilt_thumbnail.short_description = "Toote pilt"

@admin.register(Tootekategooria)
class TootekategooriaAdmin(admin.ModelAdmin):
    list_display = ('nimi',)
