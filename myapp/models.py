from django.db import models

# Create your models here.
class Student(models.Model):

    fullname=models.CharField(max_length=40)
    age= models.IntegerField(default=0)
    sex= models.CharField(max_length=10)
    nation= models.CharField(max_length=50)
    phonenumber= models.IntegerField(default=0)
    address= models.CharField(max_length=50)





    def __str__(self):

       s = " Ho ten la : " + str(self.fullname) +", Tuoi la :" + str(self.age) +", Gioi tinh :" +str(self.sex) +", Dan toc :" +str(self.nation) +", SDT:" + str(self.phonenumber) +", Dia chi:"+ str(self.address)
       return s