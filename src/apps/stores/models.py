from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return "Nombre: {}, Código postal: {}".format(self.name, self.zip_code)

class City(Location):
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

class State(Location):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Colony(Location):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'
