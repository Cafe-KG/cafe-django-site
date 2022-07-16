from django.contrib import admin

from caterings.models import Catering, BookCatering


@admin.register(Catering)
class CateringAdmin(admin.ModelAdmin):
    pass


@admin.register(BookCatering)
class CateringAdmin(admin.ModelAdmin):
    pass
