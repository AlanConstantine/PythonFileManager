from django.db import models

# Create your models here.


class Crawler(models.Model):
    name = models.CharField(max_length=120)
    crawlerfile = models.FileField(upload_to='./', null=False)
    developer = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
