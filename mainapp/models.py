from django.db import models

class ProductModel(models.Model):
    product_no = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=30, unique=True)
    product_price = models.FloatField()
    product_qnty = models.IntegerField()

    def __str__(self):
        return self.product_no

