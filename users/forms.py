
from django import forms
from .models import User, Department, UserType, Rank


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('service_number', 'rank', 'name', 'contact', 'email', 'department', 'usertype', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = 'Select Department'
        self.fields['rank'].empty_label = 'Select Rank'
        self.fields['usertype'].empty_label = 'Select UserType'





class DepartmentForm(forms.ModelForm):
  class Meta:
      model = Department
      fields = ('department_name', 'initials')


class RankForm(forms.ModelForm):
 class Meta:
    model = Rank
    fields = ('rank_name', 'initials')



class UserTypeForm(forms.ModelForm):
 class Meta:
  model = UserType
  fields = ('type_name', 'initials')


class LoginForm(forms.Form):
    username = forms
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self


        fields = ('username', 'password')