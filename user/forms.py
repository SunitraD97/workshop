from django import forms
from .models import Cars
class TestForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ('carnumber','date','name','phone','car_type')


        