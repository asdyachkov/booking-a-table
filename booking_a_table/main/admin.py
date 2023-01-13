from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.safestring import mark_safe

from .models import Salats, HotDishes, SideDishesAndSoups, Drinks, RentATable, PhotoLinks


class SalatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'cost', 'get_html_photo')
    list_display_links = ('title', 'get_html_photo')
    search_fields = ('title', 'cost')
    list_editable = ('weight', 'cost')
    list_filter = ('cost',)
    readonly_fields = ('get_html_photo',)
    fields = ('title', 'weight', 'cost', 'get_html_photo', 'photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo}' width=100>")

    get_html_photo.short_description = "Изображение"


class HotDishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'cost', 'get_html_photo')
    list_display_links = ('title', 'get_html_photo')
    search_fields = ('title', 'cost')
    list_editable = ('weight', 'cost')
    list_filter = ('cost',)
    readonly_fields = ('get_html_photo',)
    fields = ('title', 'weight', 'cost', 'get_html_photo', 'photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo}' width=100>")

    get_html_photo.short_description = "Изображение"


class RentATableAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'clients_count', 'date', 'time', 'phone_number')
    list_display_links = ('client_name', 'phone_number')
    search_fields = ('client_name', 'clients_count', 'phone_number')
    list_editable = ('clients_count', 'date', 'time')
    list_filter = ('clients_count', 'date')


class SideDishesAndSoupsAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'cost', 'get_html_photo')
    list_display_links = ('title', 'get_html_photo')
    search_fields = ('title', 'cost')
    list_editable = ('weight', 'cost')
    list_filter = ('cost',)
    readonly_fields = ('get_html_photo',)
    fields = ('title', 'weight', 'cost', 'get_html_photo', 'photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo}' width=100>")

    get_html_photo.short_description = "Изображение"


class DrinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'cost', 'get_html_photo')
    list_display_links = ('title', 'get_html_photo')
    search_fields = ('title', 'cost')
    list_editable = ('weight', 'cost')
    list_filter = ('cost',)
    readonly_fields = ('get_html_photo',)
    fields = ('title', 'weight', 'cost', 'get_html_photo', 'photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo}' width=100>")

    get_html_photo.short_description = "Изображение"


class PhotoLinksAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo',)
    list_display_links = ('get_html_photo',)
    readonly_fields = ('get_html_photo',)
    fields = ('link', 'get_html_photo')

    def get_html_photo(self, object):
        if object.link:
            return mark_safe(f"<img src='{object.link}' width=100>")

    get_html_photo.short_description = "Изображение"


AdminSite.site_title = "Админ-панель бронирование столиков"
AdminSite.site_header = "Админ-панель бронирование столиков"


admin.site.register(Salats, SalatsAdmin)
admin.site.register(HotDishes, HotDishesAdmin)
admin.site.register(SideDishesAndSoups, SideDishesAndSoupsAdmin)
admin.site.register(Drinks, DrinksAdmin)
admin.site.register(RentATable, RentATableAdmin)
admin.site.register(PhotoLinks, PhotoLinksAdmin)
