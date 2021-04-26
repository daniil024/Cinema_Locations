from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.contrib.auth.models import User


# class UserManager(BaseUserManager):
#
#     def create_user(self, username, email, password=None):
#         """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
#         if username is None:
#             raise TypeError('Users must have a username.')
#
#         if email is None:
#             raise TypeError('Users must have an email address.')
#
#         user = self.model(username=username, email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()
#
#         return user
#
#     def create_superuser(self, username, email, password):
#         """ Создает и возввращет пользователя с привилегиями суперадмина. """
#         if password is None:
#             raise TypeError('Superusers must have a password.')
#
#         if not email:
#             raise ValueError("User must have an email")
#
#         user = self.model(email=self.normalize_email(email))
#         user = self.create_user(username, email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255, unique=True, db_index=True)
#     email = models.CharField(max_length=255, unique=True, db_index=True)
#     is_verified = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.username
#
#     def tokens(self):
#         return ''


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=68, blank=True)
    last_name = models.CharField(max_length=68, blank=True)

    def __str__(self):
        return "User: {}, Phone: {}, First name: {}, Last name: {}".format(self.user, self.phone,
                                                                           self.first_name, self.last_name)


class Producer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=24, blank=True)
    last_name = models.CharField(max_length=24, blank=True)

    def __str__(self):
        return "User: {}, Phone: {}, First name: {}, Last name: {}".format(self.user, self.phone,
                                                                           self.first_name, self.last_name)


class Service(models.Model):
    # producer = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True)
    # manager = models.ForeignKey(Manager, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # оставить null=True
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    address = models.CharField(max_length=1000, null=True)
    link = models.CharField(max_length=1500, blank=True, null=True)
    price = models.IntegerField()
    contacts = models.TextField(blank=True)
    photo_link = models.CharField(max_length=20000, blank=True, null=True)
    photo1 = models.CharField(max_length=20000, blank=True, null=True)
    photo2 = models.CharField(max_length=20000, blank=True, null=True)
    photo3 = models.CharField(max_length=20000, blank=True, null=True)
    photo4 = models.CharField(max_length=20000, blank=True, null=True)
    photo5 = models.CharField(max_length=20000, blank=True, null=True)
    photo6 = models.CharField(max_length=20000, blank=True, null=True)
    photo7 = models.CharField(max_length=20000, blank=True, null=True)
    photo8 = models.CharField(max_length=20000, blank=True, null=True)
    photo9 = models.CharField(max_length=20000, blank=True, null=True)
    photo10 = models.CharField(max_length=20000, blank=True, null=True)

    def __str__(self):
        return "{}, price: {}".format(self.name, self.price)


class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)


class Ordering(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    deadline = models.DateTimeField()
    add_comments = models.CharField(max_length=400)

    def __str__(self):
        return "{}. {} - {}. Manager: {}. Producer: {}.".format(self.service.name, self.start_time, self.deadline,
                                                                self.manager, self.producer)


class Message(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    is_edited = models.BooleanField(default=False)
    message_text = models.CharField(max_length=1000)

    def __str__(self):
        return "Time: {}. Description of message: {}".format(self.datetime, self.message_text)
