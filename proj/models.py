from django.conf import settings
from django.db import models
from django.utils import timezone

class URL(models.Model):
    searchWord1 = models.TextField()
    searchWord2 = models.TextField()
    searchWord3 = models.TextField()
    WordAndOR1 = models.TextField()
    WordAndOR2 = models.TextField()
    
    Country = models.TextField()
    Status = models.TextField()

    searchInventor1 = models.TextField()
    searchInventor2 = models.TextField()
    searchInventor3 = models.TextField()
    InvAndOR1 = models.TextField()
    InvAndOR2 = models.TextField()
    URLfinal = models.TextField()
    requestDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title