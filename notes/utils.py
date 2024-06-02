# External Imports

# Django Imports

# Internal Imports


# Utility functions
def user_directory_path(instance, filename=""):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
