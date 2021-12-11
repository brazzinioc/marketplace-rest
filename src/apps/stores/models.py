from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Store(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='stores')
    domain  = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='stores/logos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comercio'
        verbose_name_plural = 'Comercios'


class StoreLocation(models.Model):
    address = models.TextField()
    number = models.IntegerField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='locations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - N° {} X,Y: {} {}".format(self.address, self.number, self.longitude, self.latitude)

    class Meta:
        verbose_name = 'Ubicación de Comercio'
        verbose_name_plural = 'Ubicacion de Comercios'


class StoreLegalDetail(models.Model):
    ruc = models.CharField(max_length=11, unique=True)
    razon_social = models.CharField(max_length=150)
    address = models.TextField()
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name='legal_detail')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.ruc, self.razon_social)

    class Meta:
        verbose_name = 'Detalle Legal de Comercio'
        verbose_name_plural = 'Detalle Legal de Comercios'

class StoreSubpage(models.Model):
    about_us = models.TextField()
    vission = models.TextField()
    mission = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='subpages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subpáginas de Comercio'
        verbose_name_plural = 'Subpáginas de Comercios'


class StoreSocialNetwork(models.Model):
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    tiktok = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='social_networks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Redes Sociales de Comercio'
        verbose_name_plural = 'Redes Sociales de Comercios'
