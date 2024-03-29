from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

class Blog(models.Model):

    # creation_date = models.DateTimeField(auto_now_add = True)

    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    
    title = models.CharField(max_length = 100,default = False)
    description = models.TextField(default = False)

    # auther = models.CharField(max_length = 100,default = False)

    def __str__(self):

        return self.title


