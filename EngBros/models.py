from django.db import models

# Create your models here.

class Products (models.Model):
    product_id =  models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory= models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")
    publish_date = models.DateField()
    image= models.ImageField(upload_to="EngBros/static/img", default="")

    def __str__(self):
        return self.product_name