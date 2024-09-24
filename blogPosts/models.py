from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
  
    def is_last_segment_number(self, s):
        last_segment = s.split('-')[-1]
        return last_segment.isdigit()

     
    def remove_last_hyphen(self, s):
        last_hyphen_index = s.rfind('-')
        if last_hyphen_index != -1: 
            return s[:last_hyphen_index]  
        return s 


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            contador = 1
            while Post.objects.filter(slug=slug).exists():
                if(self.is_last_segment_number(slug)):
                    withoutHypen = self.remove_last_hyphen(slug)
                    slug = f'{withoutHypen}-{contador}'
                    contador += 1
                else:
                    slug = f'{slug}-{contador}'
                    contador += 1
            self.slug = slug
        super(Post, self).save(*args, **kwargs)
   

    def __str__(self):
        return self.title