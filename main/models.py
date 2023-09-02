from django.db import models
from django.contrib.auth.models import User
import datetime


#add item by superuser
class Item(models.Model):
    name = models.CharField(max_length=250)
    serial_num = models.CharField(max_length=20)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    description = models.TextField()
    color = models.CharField(max_length=15)


    def __str__(self) :
        return f"Name:{self.name} Serial Number:{self.serial_num} Quantity:{self.quantity} Color:{self.color} Create_at: {self.create_at} Update_at{self.update_at} Description:{self.description}"


#taking items
class Request(models.Model):
    request_serial_number = models.IntegerField()
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    reason = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    taking_date = models.DateField()
    returning_date = models.DateField()
    list_update_at =models.DateTimeField(auto_now=True)
    # item = Item()
    quantity = models.IntegerField()
    # send_mail = models.EmailField()

    def __str__(self) :
        return f"serial_number:{self.request_serial_number} User:{self.user} Reason: {self.reason} Create at: {self.create_at} Taking date: {self.taking_date} Update at:{self.list_update_at} Returning date: {self.returning_date} Quantity: {self.quantity} "
    

# #return items
# class Return_items(models.Model):
#     request_serial_number = models.IntegerField()
#     user = models.ForeignKey(User , on_delete= models.CASCADE)
#     reason = models.TextField()
#     create_at = models.DateTimeField(auto_now_add=True)
#     taking_date = models.DateField()
#     returning_date = models.DateField()
#     list_update_at =models.DateTimeField(auto_now=True)
#     question = models.CharField(max_length=20)
#     # item = Item()
#     quantity = models.IntegerField()