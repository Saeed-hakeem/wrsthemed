from django.db import models

class User(models.Model):
    service_number = models.CharField(max_length=20, primary_key=True)
    rank = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    usertype = models.ForeignKey('UserType', on_delete=models.CASCADE)
    # noinspection PyRedeclaration
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE)
    password = models.CharField(max_length=128)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'user'


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    initials = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name

    class Meta:

        db_table = 'department'
class UserType(models.Model):
    type_name = models.CharField(max_length=50)
    initials = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'usertype'

class Rank(models.Model):
    rank_name = models.CharField(max_length=50)
    initials = models.CharField(max_length=20)

    def __str__(self):
        return self.rank_name

    class Meta:
        db_table = 'rank'