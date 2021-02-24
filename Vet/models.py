from django.db import models


class Animal(models.Model):
    races = [("1", "pitbull"), ("2", "dachshund"), ("3", "shepherd"), ("4", "yorkshire Terrier")]
    name = models.CharField(max_length=100, default="Boris")
    creation_date = models.DateField(auto_now=True)
    gender = models.BooleanField(default=True)
    race = models.CharField(max_length=100, default="1", choices=races)

    def __str__(self):
        return "Name: {0}".format(self.name)


class Doctor(models.Model):
    grades = [("1", "optometrist"), ("2", "laryngologist"), ("3", "traumatologist")]
    name = models.TextField(default="Mr.Smith")
    grade = models.CharField(max_length=100, default="1", choices=grades)

    def __str__(self):
        return "Name: {0}".format(self.name)


class Order(models.Model):
    reasons = [("1", "tachycardia"), ("2", "fracture"), ("3", "cough")]
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    reason = models.TextField(default="1", choices=reasons)

    def __str__(self):
        return "Reason: {0} Date: {1}".format(self.reason, self.date)

