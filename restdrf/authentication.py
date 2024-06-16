import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.db import models
from django.conf import settings

class AdvancedToken(Token):
    expiry_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expiry_date: 
           self.expiry_date = datetime.datetime.now() + settings.TOKEN_EXPIRY
        return super().save(*args, **kwargs) 
    
    def __str__(self):
        return self.key

class TokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    
    