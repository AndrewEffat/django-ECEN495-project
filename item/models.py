from django.db import models

# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length=100)  # column
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    quantity = models.DecimalField(max_digits=100000, decimal_places=0)
    photo = models.ImageField(upload_to='Item')  # max_length=50
    authorName = models.CharField(max_length=100)
    barcode_id = models.IntegerField(default=0)
    # reorder =
    inStock = models.IntegerField(default=0)
    deliveryDuration = models.IntegerField(default=1)

    # category = models.ForeignKey()

    def str(self):
        return self.itemName