from django.db import models

class UserFeedback(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 13)
    message = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.first_name)
