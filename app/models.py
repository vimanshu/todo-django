from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = [
    ('P','PENDING'),
    ('C', 'COMPLETED')
]

PRIORITY_CHOICES = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10','🔟')
]

class Todo(models.Model):
    title = models.CharField(max_length=255)
    status =  models.CharField(max_length=2, choices= STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    priority = models.CharField(max_length=2, choices= PRIORITY_CHOICES)
     