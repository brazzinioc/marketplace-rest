from django.db import models
from apps.cities.models import City, State, Colony


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Store(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True)
    slogan = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='category', verbose_name='Categorias')
    domain  = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='stores/logos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Comercio'
        verbose_name_plural = 'Comercios'

class StoreLocation(models.Model):
    address = models.TextField()
    number = models.IntegerField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='location', verbose_name='Comercio')
    colony = models.ForeignKey(Colony, on_delete=models.CASCADE, related_name='loc_colony', verbose_name='Colonia')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} | N°: {} | X,Y: {} {}".format(self.address, self.number, self.longitude, self.latitude)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Ubicación de Comercio'
        verbose_name_plural = 'Comercios - Ubicación'

class StoreLegalDetail(models.Model):
    ruc = models.CharField(max_length=11, unique=True)
    razon_social = models.CharField(max_length=150)
    address = models.TextField()
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name='legal_details')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.ruc, self.razon_social)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Detalle Legal de Comercio'
        verbose_name_plural = 'Comercios - Detalles Legales'

class StoreSubPage(models.Model):
    about_us = models.TextField()
    vission = models.TextField()
    mission = models.TextField()
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name='sub_pages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Subpáginas de Comercio'
        verbose_name_plural = 'Comercios - Subpáginas'

class StoreSocialNetwork(models.Model):
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    tiktok = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name='social_networks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Redes Sociales de Comercio'
        verbose_name_plural = 'Comercios - Redes Sociales'
