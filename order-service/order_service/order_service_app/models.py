from django.db import models


class Orders(models.Model):
    class Status(models.IntegerChoices):
        ISSUED = 0, 'Создан'
        DELIVERED = 1, 'Доставлен'

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_delivered = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices))
                                       , default=Status.ISSUED)
    books = models.JSONField(default=list)

    def __str__(self):
        return f'order-{self.pk}({self.time_create.strftime("%d-%m-%Y %H:%M")})'
