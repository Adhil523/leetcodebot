from django.db import models

# Create your models here.
class Questions(models.Model):
    q_id=models.IntegerField()
    q_name=models.CharField(max_length=100)
    q_desc=models.TextField()
    q_examples=models.TextField()
    q_code=models.TextField()
    q_soln=models.TextField(blank=True)
    def __str__(self):
        return self.q_name

