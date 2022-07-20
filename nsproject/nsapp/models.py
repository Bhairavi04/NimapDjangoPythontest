from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='added_to', null=True)

    def __str__(self):
        return self.project_name


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='assign_to', null=True)

    def __str__(self):
        return self.client_name
