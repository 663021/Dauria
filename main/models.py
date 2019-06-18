from django.db import models

class comments(models.Model):
    person = models.CharField(max_length = 120) #текстовый
    city = models.TextField() #текстовый
    text = models.TextField() #текстовый
    use = models.BooleanField(default=True) #логический
    data_comments = models.DateTimeField() #дата

    def __str__(self):
        return self.person

class que(models.Model):
    email = models.CharField(max_length = 120) #текстовый

    def __str__(self):
        return self.email

class news(models.Model):
    title = models.CharField(max_length = 120) #текстовый
    post = models.TextField() #текстовый
    data = models.DateTimeField() #дата

    def __str__(self):
        return self.title

    
