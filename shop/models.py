from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=600)
    category = models.CharField(max_length=500, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=30000)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name
    
    
class Contact(models.Model):
    msd_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=50, default="")
    des = models.CharField(max_length=30000,default="")

    def __str__(self):
        return self.name    
    
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json =models.CharField(max_length=9000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=5000)
    address2 = models.CharField(max_length=500, default="")  

    
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    
    def __str__(self):
        return self.name 

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."