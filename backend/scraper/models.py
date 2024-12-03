from django.db import models

# Create your models here.
class ScrapedData(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    content = models.TextField()
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title