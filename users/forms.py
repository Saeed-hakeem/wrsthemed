from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Department, UserType, Rank, Task



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




class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Service Number",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Number'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    def clean_service_number(self):
        service_number = self.cleaned_data.get('service_number')
        if User.objects.filter(service_number=service_number).exists():
            raise forms.ValidationError("This service number is already in use.")
        return service_number


class TaskAssignmentForm(forms.ModelForm):
    assigned_members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple)

    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_members', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
