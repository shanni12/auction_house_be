from django.db import models


# Create your models here.
class Products(models.Model):
    product_statuses = (("UNSOLD", "UNSOLD"), ("CLAIMED", 'CLAIMED'))
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    starting_bid = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    deadline = models.DateField(max_length=20, null=True)
    image = models.ImageField(upload_to="images", null=True)
    bids = models.TextField(default=str({}))
    uploaded_by = models.CharField(max_length=20)
    sold_to = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=10, choices=product_statuses, default="UNSOLD")
