from django.db import models
from django.utils.timezone import now
from django.conf import settings
import uuid

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, default='car make')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.id + "\t"+ self.name +"\t<"+ self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, default="car model")
    car_type = models.CharField(null=False, max_length=5, choices=CAR_TYPES, default=SEDAN)
    year = models.DateField(default=now)  
    dealer_id = models.IntegerField(default=50)

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + "\t" + self.name + "\t" + self.dealer_id + "\n" + \
        self.car_type + "\t" + self.year

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
