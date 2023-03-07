from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'


class Manager(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'manager'


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="emp", null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'


#     @classmethod
#     def show_details(cls):
#         print(f"""Get employee details for id:- {cls.id}
# emp name:- {cls.name}
# emp age:- {cls.age}
# emp salary:- {cls.salary}
# emp address:- {cls.address}
#         """)

    @staticmethod
    def active_data():
        data = Employee.objects.filter(is_active=True)
        return data

    @classmethod
    def inactive_data(cls):
        data = cls.objects.filter(is_active=False)
        return data

class CustomProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price__gt = 23000)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="prod", null=True)
    # lessprice = CustomProductManager()
    # objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'

class CustomData(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(product = 1)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    product = models.ManyToManyField(Product, related_name="cust")
    data = CustomData()
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'



from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            print("created succesfully")

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @receiver(post_delete, sender=Customer)
    def say_bye(sender, instance=None, **kwargs):
        print(f"{instance.name} is deleted successfully")



