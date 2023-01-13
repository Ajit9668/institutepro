from django.db import models

class course(models.Model):
    course_name=models.CharField(max_length=50)
    fee= models.IntegerField()
    duration=models.CharField(max_length=100)
    start_date=models.DateTimeField()
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.CharField(max_length=100)
    training_mode=models.CharField(max_length=100)

class s_table(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class feedback(models.Model):
    comment=models.TextField(max_length=500)
    date=models.DateField()


