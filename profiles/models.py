# External Imports

# Django Imports
from django.contrib.auth.models import User
from django.db import models

# Internal Imports


# Models
class ProfileSettings(models.Model):
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
        verbose_name_plural = "Profile Settings"
        unique_together = ["user", "keyword", "separator", "is_prefix"]
