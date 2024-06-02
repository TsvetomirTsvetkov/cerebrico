# External Imports

# Django Imports
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

# Internal Imports
from notes.utils import user_directory_path


# Models
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    upload = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=['md', 'txt'])])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        # Make note title url-friendly
        # self.title = self.upload.name
        if " " in self.title:
            self.title = self.title.replace(" ", "-")
            
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # TODO: Cleanup of media directory
        super().delete(*args, *kwargs)

    class Meta:
      # Make note names unique per user
      unique_together = ["user", "title"]
