from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='app_user')
    posted_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name
    
    ordering = ['-posted_at']
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
     
    @classmethod
    def all_images(cls):
        images = cls.objects.filter().order_by('-posted_at')
        return images  
         
    @classmethod
    def search_image(cls,search_term):
        """
    A method that searches an image
     """
        images = cls.objects.filter(name__icontains=search_term)
        return images    
    
    @property
    def saved_likes(self):
     return self.imagelikes.count()
 
 
    @property
    def saved_comments(self):
        return self.comments.all()  