from django.db.models.signals import pre_save
# listening for a model to save 
from django.contrib.auth.models import User

# * kwargs is keyword arg

def updateUser(sender, instance, **kwargs):
    # print('Signal triggered')
    user = instance
    if user.email != '':
        user.username = user.email

pre_save.connect(updateUser, sender=User)