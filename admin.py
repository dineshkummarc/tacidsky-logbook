from django.contrib import admin
from logbook.models import LogBookEntry, Airplane


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('flight_date','total_duration_of_flight','airport_from','airport_to','username')
    date_hierarchy = 'flight_date'
admin.site.register(LogBookEntry,LogEntryAdmin)


class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('ident', 'make','airplane_model','year')
admin.site.register(Airplane,AirplaneAdmin)
