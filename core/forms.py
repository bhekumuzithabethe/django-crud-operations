from django import forms
from .models import Position,Employee

class PositionForm(forms.ModelForm):
    
    class Meta:
        model = Position
        fields = ('position',)

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('position','first_name','last_name','email','cellphone','salary')

    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = '----Select----'