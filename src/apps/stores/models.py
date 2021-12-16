from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from apps.cities.models import Colony


class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    historical = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'status']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Store(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True)
    slogan = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='categories', verbose_name='Categorias')
    logo = models.ImageField(upload_to='stores/logos', default='stores/logos/no-logo.png')
    historical = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at', 'status']
        verbose_name = 'Comercio'
        verbose_name_plural = 'Comercios'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class StoreLocation(BaseModel):
    address = models.TextField()
    number = models.IntegerField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    store = models.OneToOneField(Store, on_delete=models.CASCADE, verbose_name='Comercio')
    colony = models.ForeignKey(Colony, on_delete=models.RESTRICT, related_name='colony', verbose_name='Colonia')
    historical = HistoricalRecords()

    def __str__(self):
        return "{} | N°: {} | X,Y: {} {}".format(self.address, self.number, self.longitude, self.latitude)

    class Meta:
        ordering = ['created_at', 'status']
        verbose_name = 'Ubicación de Comercio'
        verbose_name_plural = 'Comercios - Ubicación'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class StoreLegalDetail(BaseModel):
    ruc = models.CharField(max_length=11, unique=True)
    razon_social = models.CharField(max_length=150)
    address = models.TextField()
    store = models.OneToOneField(Store, on_delete=models.CASCADE, verbose_name='Comercio')
    historical = HistoricalRecords()

    def __str__(self):
        return "{} - {}".format(self.ruc, self.razon_social)

    class Meta:
        ordering = ['created_at', 'status']
        verbose_name = 'Detalle Legal de Comercio'
        verbose_name_plural = 'Comercios - Detalles Legales'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class StoreSubPage(BaseModel):
    about_us = models.TextField()
    vission = models.TextField()
    mission = models.TextField()
    store = models.OneToOneField(Store, on_delete=models.CASCADE, verbose_name='Comercio')
    historical = HistoricalRecords()

    class Meta:
        ordering = ['created_at', 'status']
        verbose_name = 'Subpáginas de Comercio'
        verbose_name_plural = 'Comercios - Subpáginas'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class StoreSocialNetwork(BaseModel):
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    tiktok = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    store = models.OneToOneField(Store, on_delete=models.CASCADE, verbose_name='Comercio')
    historical = HistoricalRecords()

    class Meta:
        ordering = ['created_at', 'status']
        verbose_name = 'Redes Sociales de Comercio'
        verbose_name_plural = 'Comercios - Redes Sociales'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value



