from django.db import models
import datetime

# Create your models here.

class  Post(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
             return self.title

    class meta:
        verbose_name_plural = 'my_post'
        db_table = 'post'

        

class Question(models.Model):
    Question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class meta:
        verbose_name_plural = 'questions'
        db_table = 'questions'

    def __str__(self):
        return self.Question
                
        
