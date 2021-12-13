from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import Location


class City(Location):
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class State(Location):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='state', verbose_name='Ciudad')
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Colony(Location):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='colony', verbose_name='Estado')
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
