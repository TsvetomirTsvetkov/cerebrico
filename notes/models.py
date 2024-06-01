from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


def user_directory_path(instance, filename=""):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    upload = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=['md', 'txt'])])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        # Make file title url-friendly
        # self.title = self.upload.name
        if " " in self.title:
            self.title = self.title.replace(" ", "-")
            
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # TODO: Cleanup of media directory
        super().delete(*args, *kwargs)

    class Meta:
      # Make file names unique per user
      unique_together = ["user", "title"]

class UserSettings(models.Model):
    CHECKBUTTON = "CB"

    TYPE_CHOICES = {
        CHECKBUTTON: "CheckButton",
    }
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.CharField(max_length=250)
    type = models.CharField(choices=TYPE_CHOICES, default=CHECKBUTTON)
    keyword = models.CharField(max_length=50)
    separator = models.CharField(max_length=2)
    is_prefix = models.BooleanField(default=False)

    def __str__(self):
        return str(self.option)
    
    def __repr__(self):
        if self.is_prefix:
            return self.separator + self.keyword
        else:
            return self.keyword + self.separator

    class Meta:
        verbose_name_plural = "User Settings"
        unique_together = ["keyword", "separator", "is_prefix"]

