from django.db import models

# Create your models here.

class Allcourse(models.Model):
    coursename= models.CharField(max_length=200)
    insname= models.CharField(max_length=100)
    def __str__(self):
        return self.coursename
class detail(models.Model):
    couse= models.ForeignKey(Allcourse,  on_delete= models.CASCADE)
    sp= models.CharField(max_length=100)
    il= models.CharField(max_length=400)
    def __str__(self):
        return self.sp

