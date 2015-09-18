from django.contrib import admin
from .models import Gamers
class GamersAdmin(admin.ModelAdmin):

    def upper_case_name(obj):
        return ("%s %s" % (obj.FirstName, obj.LastName)).upper()
        upper_case_name.short_description = 'Name'


    list_display = (upper_case_name,)

admin.site.register(Gamers, GamersAdmin)


# Register your models here.
