from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Blog(models.Model):
    name=models.CharField(max_length=50)
    para=models.TextField(max_length=10000)
    image=models.ImageField(upload_to="uploads/image",default="")
    time=models.DateTimeField(blank=True,null=True)
    author=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name
    


    