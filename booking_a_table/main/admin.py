from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Salats, HotDishes, SideDishesAndSoups, Drinks, RentATable, PhotoLinks


class SalatsResource(resources.ModelResource):

    class Meta:
        model = Salats
        fields = ('id', 'title', 'weight', 'cost', 'photo')
        exclude = ('imported',)


class SalatsForAdminSecond(ImportExportModelAdmin):
    resource_class = SalatsResource


class SalatsForAdmin(TranslationAdmin):
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


class SalatsAdmin(SalatsForAdmin, SimpleHistoryAdmin, SalatsForAdminSecond):
    pass


class HotDishesResource(resources.ModelResource):

    class Meta:
        model = HotDishes
        fields = ('id', 'title', 'weight', 'cost', 'photo')
        exclude = ('imported',)


class HotDishesForAdminSecond(ImportExportModelAdmin):
    resource_class = HotDishesResource


class HotDishesForAdmin(TranslationAdmin):
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

class HotDishesAdmin(HotDishesForAdmin, SimpleHistoryAdmin, HotDishesForAdminSecond):
    pass


class RentATableResource(resources.ModelResource):

    class Meta:
        model = RentATable
        fields = ('id', 'client_name', 'clients_count', 'date', 'time', 'phone_number')
        exclude = ('imported',)


class RentATableForAdminSecond(ImportExportModelAdmin):
    resource_class = RentATableResource


class RentATableForAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'clients_count', 'date', 'time', 'phone_number')
    list_display_links = ('client_name', 'phone_number')
    search_fields = ('client_name', 'clients_count', 'phone_number')
    list_editable = ('clients_count', 'date', 'time')
    list_filter = ('clients_count', 'date')


class RentATableAdmin(RentATableForAdmin, SimpleHistoryAdmin, RentATableForAdminSecond):
    pass


class SideDishesAndSoupsResource(resources.ModelResource):

    class Meta:
        model = SideDishesAndSoups
        fields = ('id', 'title', 'weight', 'cost', 'photo')
        exclude = ('imported',)


class SideDishesAndSoupsForAdminSecond(ImportExportModelAdmin):
    resource_class = SideDishesAndSoupsResource


class SideDishesAndSoupsForAdmin(TranslationAdmin):
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

class SideDishesAndSoupsAdmin(SideDishesAndSoupsForAdmin, SimpleHistoryAdmin, SideDishesAndSoupsForAdminSecond):
    pass


class DrinksResource(resources.ModelResource):

    class Meta:
        model = Drinks
        fields = ('id', 'title', 'weight', 'cost', 'photo')
        exclude = ('imported',)


class DrinksForAdminSecond(ImportExportModelAdmin):
    resource_class = DrinksResource


class DrinksForAdmin(TranslationAdmin):
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


class DrinksAdmin(DrinksForAdmin, SimpleHistoryAdmin, DrinksForAdminSecond):
    pass


class PhotoLinksResource(resources.ModelResource):

    class Meta:
        model = PhotoLinks
        fields = ('id', 'link')
        exclude = ('imported',)


class PhotoLinksForAdminSecond(ImportExportModelAdmin):
    resource_class = PhotoLinksResource


class PhotoLinksForAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo',)
    list_display_links = ('get_html_photo',)
    readonly_fields = ('get_html_photo',)
    fields = ('link', 'get_html_photo')

    def get_html_photo(self, object):
        if object.link:
            return mark_safe(f"<img src='{object.link}' width=100>")

    get_html_photo.short_description = "Изображение"


class PhotoLinksAdmin(PhotoLinksForAdmin, SimpleHistoryAdmin, PhotoLinksForAdminSecond):
    pass


AdminSite.site_title = "Админ-панель бронирование столиков"
AdminSite.site_header = "Админ-панель бронирование столиков"


admin.site.register(Salats, SalatsAdmin)
admin.site.register(HotDishes, HotDishesAdmin)
admin.site.register(SideDishesAndSoups, SideDishesAndSoupsAdmin)
admin.site.register(Drinks, DrinksAdmin)
admin.site.register(RentATable, RentATableAdmin)
admin.site.register(PhotoLinks, PhotoLinksAdmin)
