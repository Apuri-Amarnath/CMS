import tinymce.models
from django.db import models
import uuid
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Blog_post(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='img')
    body = HTMLField()
    post_id = models.UUIDField(default=uuid.uuid4(),primary_key=True,unique=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User,related_name='Likes')

    def __str__(self):
        return self.title

