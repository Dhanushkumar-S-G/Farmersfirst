from django.db import models



class Product(models.Model):
    id = models.CharField(verbose_name="Product name",primary_key=True,max_length=255)
    imagelink = models.TextField(verbose_name="Image link")
    price = models.TextField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    category = models.TextField(verbose_name="category",max_length= 255)
    rating = models.IntegerField(verbose_name="Ratings")
    

    def __str__(self):
        return self.id


class Cart(models.Model):
    user_phonenumber = models.TextField(verbose_name="phone_number") 
    productname = models.TextField(verbose_name="productname")
    quantity = models.TextField(verbose_name="quantity",default='1')
    price = models.IntegerField(verbose_name="price",default=00)

