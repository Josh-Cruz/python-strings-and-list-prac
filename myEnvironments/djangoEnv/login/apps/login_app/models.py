from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        results = {}
        if len(postData['first_name']) < 3:
            results["first_name"] = "First name should be more than 3 characters"
        if len(postData['last_name']) < 3:
            results['last_name'] = "Last name should be more than 3 characters"      
        if not EMAIL_REGEX.match(postData['email']):
            results['email'] = 'E-mail address invalid'
        if postData['password'] != postData['confirm_password']:
            results['password'] = 'Passwords must match'
        
        # results will either be a dict(fail[has error]) or a int(pass[no errors])
        if results:
            return results

        # check to see if user exists
        try:
            existing_user = self.get(email=postData['email'])
            results['email']= 'E-mail already exists!'
            return results
        except:
            pw_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(first_name=postData['first_name'],last_name=postData['last_name'], email=postData['email'], password=pw_hash )
            return user.id

    def login_user(self, postData):
        results = {}
        try:
            # print "i tried"
            user = self.get(email=postData['email'])
            # print "user worked"
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                # print "passwords match" 
                return user.id
        except:
            # print "in except statement"
            results['error'] = 'E-mail or Password are incorrect'
            return results
        else:
            # print "in else statement"
            return user.id   
        


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()