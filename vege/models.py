from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Receipe(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reciepe_name=models.CharField(max_length=100)
    reciepe_description=models.TextField()
    reciepe_image=models.ImageField(upload_to='reciepe')
    reciepe_view_count=models.IntegerField(default=1)
