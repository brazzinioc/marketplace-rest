from django.db import models
from django.contrib import admin

# Create your models here.
class BaseModel(models.Model):
    """
    BaseModel is the base model for all models.
    """
    status = models.BooleanField('Estado', default=True)
    created_at = models.DateTimeField('Creado el', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado el', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Location(BaseModel):
    name = models.CharField('Nombre', max_length=255)
    zip_code = models.CharField('Código Postal', max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class LocationAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_display = [ 'name', 'zip_code', 'status', 'created_at', 'updated_at' ]
        self.list_filter = [ 'name', 'zip_code', 'status', 'created_at', 'updated_at' ]

    class Meta:
        abstract = True
