from django.contrib import admin
from apps.base.models import LocationAdmin
from apps.cities.models import City, State, Colony


class CityAdmin(LocationAdmin):
    pass

class StateAdmin(LocationAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_display.append('city')
        self.list_filter.append('city')

class ColonyAdmin(LocationAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_display.append('state')
        self.list_filter.append('state')


admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Colony, ColonyAdmin)

