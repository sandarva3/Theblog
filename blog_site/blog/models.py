from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id = str(instance.author.id), title = str(instance.title), filename=filename
    )
    return file_path

class Blogpost(models.Model):
    title = models.CharField(max_length=75,null=False,blank=False)
    body = models.CharField(max_length=6500,null=False,blank=False)
    image = models.ImageField(upload_to=upload_location,null=False,blank=False)
    date_published = models.DateTimeField(auto_now=True,verbose_name ="date published")
    date_update = models.DateTimeField(auto_now_add=True,verbose_name = "date update")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,unique=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Blogpost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender = Blogpost)
        



    


