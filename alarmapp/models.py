from django.db import models

# Create your models here.
class weblink(models.Model):
    user=models.CharField('Username',max_length=120)
    cmd=models.CharField('UserCommand',max_length=120)
    url=models.CharField('Weburl',max_length=200)
    def __str__(self):
        return self.url
class timetable(models.Model):
    user=models.CharField('Username',max_length=120)
    day_name=models.CharField('day_name', max_length=120)
    eight_to_nine=models.CharField('8 to 9',max_length=120)
    nine_to_ten=models.CharField('9 to 10',max_length=120)
    ten_to_eleven=models.CharField('10 to 11',max_length=120)
    eleven_to_twelve=models.CharField('11 to 12',max_length=120)
    twelve_to_one=models.CharField('12 to 1',max_length=120)
    two_to_three=models.CharField('2 to 3',max_length=120)
    three_to_four=models.CharField('3 to 4',max_length=120)
    four_to_five=models.CharField('4 to 5',max_length=120)
class subjects(models.Model):
    user=models.CharField('username',max_length=120)
    subject=models.CharField('subject_name',max_length=120)
class days(models.Model):
    name=models.CharField('dayname',max_length=120)
class times(models.Model):
    timeing=models.CharField('time',max_length=120)
    timenum=models.CharField('time in numbers',max_length=120)
class Users(models.Model):
    username=models.CharField('Username',max_length=120)
    pwd=models.CharField('Password',max_length=120)