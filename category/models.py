from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    # purchaseItem()
    # addItem()
    # removeItem()
    # editItem()
    # reorder()
    # email()
    
    def __str__(self):
        return self.categoryName