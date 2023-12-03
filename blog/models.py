from django.db import models

from accounts.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    published = models.BooleanField(default=True, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name="owned_posts")

    def __str__(self):
        return self.title
    
    # Na Classe Meta, nós podemos incluir meta-dados. 
    class Meta:
        ordering = ["-date"] # Sempre que dermos uma query em Post, vai ordenar pela mais recente.
        # order_by("-date")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=False, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name="comments_made")
    content = models.TextField(null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} | {self.post}"