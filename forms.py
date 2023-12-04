# forms.py
from django import forms
from .models import Applicant
from .models import AddCrops
from .models import ApplyScheme

# class ApplicantForm(forms.ModelForm):
#     class Meta:
#         model = Applicant
#         fields = ['Applicant_Name' , 'address', 'aadhar_card', 'ration_card','monthly_income']

class ApplicationView(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['Applicant_Name', 'monthly_income', 'address', 'aadhar_card', 'ration_card', 'status']

        widgets = {
            'Applicant_Name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'monthly_income': forms.TextInput(attrs={'readonly': 'readonly'}),
            'address': forms.Textarea(attrs={'readonly': 'readonly'}),
            'aadhar_card': forms.ClearableFileInput(attrs={'readonly': 'readonly'}),
            'ration_card': forms.ClearableFileInput(attrs={'readonly': 'readonly'}),
            'status': forms.Select(),
        }
# forms.py
from django import forms
from .models import AddCrops  # Import your model

class AddCropsForm(forms.ModelForm):
    class Meta:
        model = AddCrops
        fields = '__all__'  # Include all fields from the model
        # Or specify fields explicitly: fields = ['cname', 'desc', ...]

        
from django import forms
from .models import AddCrops  # Import your model

class ApplySchemeForm(forms.ModelForm):
    class Meta:
        model = ApplyScheme
        fields = '__all__'  # Include all fields from the model
        # Or specify fields explicitly: fields = ['cname', 'desc', ...]
