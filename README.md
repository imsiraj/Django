# Django Project with Custom Rectangle Class and Signals

This project showcases a Django application that includes a custom `Rectangle` class in Python and explores the use of Django signals. The project also provides insights into various aspects of Django, such as signal handling and database transactions.
## Features
- **Rectangle Class**: A custom class to represent rectangles, allowing for iteration over its dimensions.
- **Django Signals**: Demonstrates how to use Django signals to trigger actions on model events.
- **Database Transactions**: Explores how Django handles transactions with signals.


## Questions Addressed

### 1. Are Django signals executed synchronously or asynchronously?
- **Answer**: By default, Django signals are executed synchronously, meaning the signal handlers run in the same thread and process as the caller. This ensures that any side effects caused by the signal handlers are completed before control returns to the caller.

  Here’s a simple example to demonstrate this:

  ```python
  from django.db.models.signals import post_save
  from django.dispatch import receiver
  from myapp.models import MyModel

  @receiver(post_save, sender=MyModel)
  def my_model_post_save(sender, instance, **kwargs):
      print(f"Signal triggered: {instance.name}")

### 2. Do Django signals run in the same thread as the caller?
**Answer**: Yes, Django signals run in the same thread as the caller by default, ensuring that the signal handlers execute in the same context as the calling code. This is important for maintaining the state and context in which the signal was triggered.

### 3. Do Django signals run in the same database transaction as the caller?
**Answer**: No, Django signals do not run in the same database transaction as the caller. Changes made in signal handlers are committed independently of the transaction that triggered the signal. This means that if an error occurs in the signal handler, it does not affect the caller's transaction.
