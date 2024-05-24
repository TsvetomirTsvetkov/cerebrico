from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename=""):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    upload = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        self.title = self.title.replace(" ", "-")        
        super().save(*args, **kwargs)

    class Meta:
      unique_together = 'user', 'title'


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
