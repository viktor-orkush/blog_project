from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.CharField('auth.User', max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_data = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approve_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs = {'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
