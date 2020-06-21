from django.db import models

# Create your models here.

class Publisher(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    first_name = models.CharField(max_length = 100, blank=False)
    last_name = models.CharField(max_length = 100, blank=False)
    middle_name = models.CharField(max_length = 100, blank = True) 
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name 

class Story(models.Model):
    story_id = models.CharField(max_length=100, primary_key=True, unique=True)
    title = models.CharField(max_length=100, blank=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=400, blank=False)
    
    def __str__(self):
        return self.story_id + ' by ' + self.publisher.first_name
       
    
    
class Content(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    pub_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.story.story_id
    
