from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename=""):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    upload = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


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

    class Meta:
        verbose_name_plural = "User Settings"
