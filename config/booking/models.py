from django.db import models

class Booking(models.Model):
    CITY_CHOICES = (
    (1, "Могилёв"),
    (2, "Шклов"),
    (3, "Бобруйск"),
    (4, "Гомель"),
    (5, "Орша")
    )

    AIRPORT_CHOICES = (
        (1, "а/п Борисполь"),
        (2, "а/п Шереметьево"),
        (3, "а/п Внуково"),
        (4, "а/п Домодедово"),
        (5, "а/п Остафьево"),
        (6, "а/п Жуковский"),
    )

    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=30)
    city = models.IntegerField(choices=CITY_CHOICES, default=1)
    airport = models.IntegerField(choices=AIRPORT_CHOICES, default=1)
    count = models.PositiveIntegerField(default=1)
    order_date = models.DateField()
    is_back = models.BooleanField(default=True)
    back_date = models.DateField()
    notes = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.count} {self.order_date}'


class Direction(models.Model):
    CITY_CHOICES = (
    (1, "Могилёв"),
    (2, "Шклов"),
    (3, "Бобруйск"),
    (4, "Гомель"),
    (5, "Орша")
    )

    AIRPORT_CHOICES = (
        (1, "а/п Борисполь"),
        (2, "а/п Шереметьево"),
        (3, "а/п Внуково"),
        (4, "а/п Домодедово"),
        (5, "а/п Остафьево"),
        (6, "а/п Жуковский"),
    )

    city = models.IntegerField(choices=CITY_CHOICES, default=1)
    airport = models.IntegerField(choices=AIRPORT_CHOICES, default=1)
    price = models.IntegerField(default=1)
    is_child = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.get_city_display()} {self.get_airport_display()} {self.is_child} {self.price}'

    class Meta:
        unique_together = ['city','airport','is_child']