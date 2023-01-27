
from django.db import models
import uuid
# Create your models here.
class Order(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    order_amount=models.IntegerField(null=True,blank=True,default=0)
    order_meta=models.CharField(max_length=100,blank=True,null=True,default="")

    class meta :
        verbose_name='Order'
