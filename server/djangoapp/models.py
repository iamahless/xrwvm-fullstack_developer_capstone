# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make
    country = models.CharField(max_length=50, blank=True, null=True)  # Optional: Country

    def __str__(self):
        return f"{self.name} - {self.description}"

class CarModel(models.Model):
    TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-one relationship
    dealer_id = models.IntegerField()  # Refers to a dealer ID in Cloudant database
    name = models.CharField(max_length=100)  # Name of the car model
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='SUV')  # Type of the car
    year = models.IntegerField()  # Manufacturing year
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional: Price of the car

    def __str__(self):
      return f"CarModel(name='{self.name}', car_type='{self.type}', year={self.year}, make='{self.car_make.name}')"