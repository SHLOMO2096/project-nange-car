from django.db import models

# Create your models here.
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)  # מותג הרכב
    model = models.CharField(max_length=50)  # דגם
    year = models.IntegerField()  # שנת ייצור
    daily_rental_price = models.DecimalField(max_digits=10, decimal_places=2)  # מחיר השכרה ליום
    available = models.BooleanField(default=True)  # האם הרכב זמין להשכרה

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Customer(models.Model):
    name = models.CharField(max_length=100)  # שם הלקוח
    phone = models.CharField(max_length=15)  # מספר טלפון
    license_number = models.CharField(max_length=20, unique=True)  # מספר רישיון נהיגה

    def __str__(self):
        return self.name


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # הרכב שהושכר
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # הלקוח ששכר
    start_date = models.DateField()  # תאריך תחילת ההשכרה
    end_date = models.DateField()  # תאריך סיום ההשכרה
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # מחיר כולל להשכרה

    def save(self, *args, **kwargs):
        """ חישוב מחיר ההשכרה לפי מספר הימים והמחיר היומי של הרכב """
        if self.start_date and self.end_date and self.car:
            num_days = (self.end_date - self.start_date).days
            self.total_price = num_days * self.car.daily_rental_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Rental of {self.car} by {self.customer} from {self.start_date} to {self.end_date}"

