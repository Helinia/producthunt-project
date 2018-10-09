from django.db import models
from django.contrib.auth.models import User





class Product(models.Model):
    #title
    title = models.CharField(max_length = 255)
    #url
    url = models.TextField()
    #pub_date
    pub_date = models.DateTimeField()
    #votes_total
    votes_total = models.IntegerField(default = 1)
    #image
    image = models.ImageField(upload_to = 'images/')
    #icon
    icon = models.ImageField(upload_to = 'images/')
    #body
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
