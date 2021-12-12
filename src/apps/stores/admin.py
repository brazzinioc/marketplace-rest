from django.contrib import admin
from apps.stores.models import Category, Store, StoreLocation, StoreLegalDetail, StoreSubPage, StoreSocialNetwork


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    list_filter = [ 'name', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'slogan', 'get_categories', 'domain', 'logo', 'created_at', 'updated_at']
    list_filter = [ 'name', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}

    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.category.all()])

class StoreLocationAdmin(admin.ModelAdmin):
    list_display = ['store', 'address', 'colony', 'created_at', 'updated_at']
    list_filter = ['colony', 'created_at', 'updated_at']

class StoreLegalDetailAdmin(admin.ModelAdmin):
    list_display = ['store', 'ruc', 'razon_social', 'address', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

class StoreSubPageAdmin(admin.ModelAdmin):
    list_display = ['store', 'about_us', 'vission', 'mission', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

class StoreSocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['store', 'facebook', 'instagram', 'tiktok', 'twitter', 'youtube', 'whatsapp',  'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(StoreLocation, StoreLocationAdmin)
admin.site.register(StoreLegalDetail, StoreLegalDetailAdmin)
admin.site.register(StoreSubPage, StoreSubPageAdmin)
admin.site.register(StoreSocialNetwork, StoreSocialNetworkAdmin)
