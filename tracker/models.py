from django.db import models

# Create your models here.



class card(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add= True)
    
class info(models.Model):
    type = [("income","income"),("expense","expense")]
    
    title = models.CharField(max_length=25)
    description = models.TextField()
    amount = models.PositiveIntegerField()
    entry_type = models.CharField(choices=type,default="income",max_length=25)
    card = models.ForeignKey(card,on_delete=models.CASCADE,related_name="cards")