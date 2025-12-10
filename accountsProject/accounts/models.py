from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    ''' A custom user model.
        We use AbstractUser because Django handles passwords, authentication,
        and default fields (username, password, first_name, last_name, email) in advance.
        We add a role field for managing simple permissions (User/Admin).
    '''

    role_user = "user"
    role_admin = "admin"
    role_choices = [
        (role_user, "User"),
        (role_admin, "Admin"),
    ]
    email = models.EmailField(unique=True)

    # the role of user
    role = models.CharField(
        max_length=10,
        choices=role_choices,
        default=role_user,
        help_text="Role of the user: user or admin",
    )

    # to upload profile_img
    profile_image = models.ImageField(upload_to="profiles/", null=True, blank=True)

    def is_admin(self):
        # to check if the user is admin
        return self.role == self.role_admin or self.is_superuser

    def __str__(self):
        return f"{self.username} ({self.email})"
