from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import datetime
from django.utils import timezone


from django.utils.timezone import utc

now = datetime.datetime.utcnow().replace(tzinfo=utc)
# Create your models here.
class User(AbstractUser):

    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^[6-9][0-9]{9}$',
                                 message="Phone number must be entered in the format: '9999999999'. Only 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','username']
    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
class State(models.Model):
    state = models.CharField(max_length=30)
    def __str__(self):
        return self.state

class RequestType(models.Model):
    requesttype = models.CharField(max_length=100)
    def __str__(self):
        return self.requesttype
class Status(models.Model):
    status = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.status
class RequestList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requesttype = models.ManyToManyField(RequestType)
    requestdesc = models.TextField()
    city = models.TextField()
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=10)
    countrycode = models.CharField(max_length=10)

    phone_number = models.CharField(max_length=10)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    remarks = models.TextField()
    updated_by =  models.ForeignKey(User,on_delete=models.CASCADE,related_name="updated_by",default=1)
    updated_at = models.DateTimeField(default=now)
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return self.pk

