from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=8)
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=300, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        #como se va a comportar una clase
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.title}'