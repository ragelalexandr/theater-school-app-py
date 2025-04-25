from django.db import models

# Create your models here.

class PortfolioItem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolio_items')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    media_file = models.FileField(upload_to='portfolio/', blank=True, null=True)
    media_url = models.URLField(blank=True, null=True)  # если видео хостится на YouTube или Vimeo
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
