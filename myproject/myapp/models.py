from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import threading
class MyModel(models.Model):
    name = models.CharField(max_length=100)

class AnotherModel(models.Model):
    related_name = models.CharField(max_length=100)
    
# 1st question -answer
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal received. Starting delay...")
    time.sleep(5)  # Simulate a delay
    print("Delay finished.")


# 2nd question -answer -for threading
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")
    time.sleep(5)  # Simulate a delay
    print("Delay finished in thread:", threading.current_thread().name)



@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    # Attempt to create another model instance in the signal
    AnotherModel.objects.create(related_name="Created from signal")
