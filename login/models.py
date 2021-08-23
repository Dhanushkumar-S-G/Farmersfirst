from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField, TextField


class UserManager(BaseUserManager):
    def create_user(self, user_name, phone_number, email,address,pincode, password=None):
        user = self.model(
            user_name=user_name,
            phone_number=phone_number,
            email=email,
            address = address,
            pincode = pincode
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, phone_number, password, email,address,pincode):
        user = self.create_user(
            user_name=user_name,
            password=password,
            phone_number=phone_number,
            email=email,
            address = address,
            pincode = pincode   )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone_number = models.BigIntegerField(
        verbose_name="Phone number",  unique=True, primary_key=True)
    user_name = models.CharField(verbose_name="User name", max_length=64)
    date_joined = models.DateTimeField(
        verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="Last login", auto_now_add=True)
    email = models.EmailField(verbose_name="email")
    address = models.TextField(verbose_name="address")
    pincode = models.CharField(verbose_name="pincode",max_length=6)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["user_name", "password", "email","pincode","address"]

    object = UserManager()

    def __str__(self):
        return "{} \t {}".format(self.phone_number, self.user_name)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Order(models.Model):
    user = models.TextField(verbose_name="User name")
    product_name = models.TextField(verbose_name="Product Name",max_length=255)
    quantity = models.IntegerField(verbose_name="Quantity")
    price = models.IntegerField(verbose_name="price")
    date_ordered = models.DateTimeField(verbose_name="Date ordered",auto_now_add=True)
    date_required = models.DateField(verbose_name="Date required")
    address = models.TextField(verbose_name="Address")

    def __str__(self):
        return f'{self.date_required}  {self.product_name}  {self.quantity}'


    