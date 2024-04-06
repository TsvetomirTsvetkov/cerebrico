from django.db import models

# TODO: Create DB Models here

class File(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to="uploads/")
