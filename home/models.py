from django.db import models

class Jewelry(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='jewelry/')
    
class JewelryPrice(models.Model):
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
