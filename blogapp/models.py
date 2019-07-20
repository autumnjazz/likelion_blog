from django.db import models
from django.utils import timezone 


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    class Meta:
        ordering = ['-id'] #id의 역순으로 순서



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    #foreignkey 는 일대다 관계. post와 comment의 관계
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-id'] #id의 역순으로 순서