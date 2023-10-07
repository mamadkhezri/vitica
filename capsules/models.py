from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify

class TimeCapsule(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message_related = models.TextField()
    publication_date = models.DateField()
    slug = models.SlugField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    tags = TaggableManager()
    

    def __str__(self):
        return self.title

class Photo(models.Model):
    time_capsule = models.ForeignKey(TimeCapsule, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')  # This field stores the photo file

    def __str__(self):
        return self.photo.name

class Sound(models.Model):
    time_capsule = models.ForeignKey(TimeCapsule, on_delete=models.CASCADE)
    sound = models.FileField(upload_to='sounds/')  # This field stores the sound file

    def __str__(self):
        return self.sound.name

class Video(models.Model):
    time_capsule = models.ForeignKey(TimeCapsule, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')  # This field stores the video file

    def __str__(self):
        return self.video.name

class Message(models.Model):
    time_capsule = models.ForeignKey(TimeCapsule, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"Message in {self.time_capsule.title}"

class Document(models.Model):
    time_capsule = models.ForeignKey(TimeCapsule, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')  # This field stores the document file

    def __str__(self):
        return self.document.name
    

    def get_absolute_url(self):
        print("PK:", self.pk)
        print("Slug:", self.slug)
        url = reverse('capsules:capsule_detail', args=[str(self.pk), self.slug])
        print("Generated URL:", url)
        return url
    
    def user_can_like(self, user):
        return user.uvotes.filter(post=self).exists()
    

class vote(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uvotes')
    time_capsule = models.ForeignKey(TimeCapsule, on_delete=models.CASCADE, related_name='pvotes')

    def __str__(self):
        return f'{self.author} liked {self.post}'
    

class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_comments')
    capsule = models.ForeignKey(TimeCapsule, on_delete=models.CASCADE, related_name='post_comments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply_comments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    comment = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

