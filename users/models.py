from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, service_number, rank, name, contact, email, department, usertype,  password=None,
                    **extra_fields):
        if not service_number:
            raise ValueError('The Service Number is required')
        if not name:
            raise ValueError('name is required')
        if not email:
            raise ValueError('The Email must is required')
        if not department:
            raise ValueError('provide department')
        if not contact:
            raise ValueError('please provide an active contact number')
        if not department:
            raise ValueError('department is required')
        if not rank:
            raise ValueError('rank is required')
        if not usertype:
            raise ValueError('usertype is required')



        user = self.model(service_number=service_number,
                          rank=rank,
                          name=name,
                          contact=contact,
                          email=self.normalize_email(email),
                          department=department,
                          usertype=usertype,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, service_number, rank, name, contact, email, department, usertype, password=None):
        user = self.create_user(
            service_number=service_number,
            rank=rank,
            name=name,
            contact=contact,
            email=email,
            department=department,
            usertype=UserType,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    service_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField(null=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)
    usertype = models.ForeignKey('UserType', on_delete=models.CASCADE, null=True)
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = 'service_number'
    REQUIRED_FIELDS = ['rank', 'name', 'contact', 'email', 'department', 'usertype',]

    def __str__(self):
        return self.name

    def has_perms(self, perm_list, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


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

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_members = models.ForeignKey('User', on_delete=models.CASCADE, related_name='assigned_members')
    due_date = models.DateField()
    priority = models.CharField(max_length=50)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'task'