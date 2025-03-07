from django.db import models

# Create your models here.


from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=25)
    anime = models.CharField(max_length=25)
    is_trending=models.BooleanField()
    image = models.ImageField(upload_to='media', max_length=175)

    def __str__(self):
        return self.name




class User(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    image=models.ImageField(upload_to='media', default='./default_profile_image.png')

    # objects = CustomUserManager()

    def __str__(self):
        return self.email


class current_user(models.Model):
    id=models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    image=models.ImageField(upload_to='media')

    # objects = CustomUserManager()

    def __str__(self):
        return self.email



class Cart(models.Model):
    name=models.CharField(max_length=50)
    price=models.ImageField()
    quantity=models.ImageField()
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class Anime(models.Model):
    name=models.CharField(max_length=25, unique=True)
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=25, unique=True)
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=25, unique=True)
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
