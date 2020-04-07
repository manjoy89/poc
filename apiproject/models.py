from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200,null=False,default='Product Name')
    productDesc = models.CharField(max_length=300,null=False,default='Product Disc')
    productLink = models.CharField(max_length=300,null=False,default='Product Link')
    productPrice = models.DecimalField(max_digits=5, decimal_places=2,default='0.00')
    productSite = models.CharField(max_length=100,null=False,default='Product Site')

