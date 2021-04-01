from django.db import models
from django.contrib.auth.models import User


class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "User: {}, Phone: {}".format(self.user, self.phone)


class Producer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "User: {}, Phone: {}".format(self.user, self.phone)


class Service(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    price = models.IntegerField()
    # photo = models.ImageField(blank=True, null=True)

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