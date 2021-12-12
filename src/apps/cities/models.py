from django.db import models


class Location(models.Model):
    name = models.CharField('Nombre', max_length=255)
    zip_code = models.CharField('Código Postal', max_length=255)
    created_at = models.DateTimeField('Creado el', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado el', auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class City(Location):
    pass

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'


class State(Location):
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='state', verbose_name='Ciudad')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Colony(Location):
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='colony', verbose_name='Estado')

    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'
