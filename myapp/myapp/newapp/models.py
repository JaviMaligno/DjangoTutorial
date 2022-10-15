from django.db import models

# Create your models here.
class Members(models.Model):
    #This will be used to create a table with two fields. To do it run
    # py manage.py makemigrations newapp
    # This creates a file in /migrations
    #  Then we run
    # py manage.py migrate
    # to run the SQL commands that create the table
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)