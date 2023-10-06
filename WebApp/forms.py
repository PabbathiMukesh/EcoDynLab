from django import forms
from django.forms import widgets
from django.contrib.auth import get_user_model
from .models import Image, Agency, Project, ImageFolder
# from django_select2.forms import Select2Widget
User = get_user_model()

from WebApp.models import Station

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):  # Use ModelForm instead of forms.Form
    class Meta:
        model = User  # Use the User model as the base
        fields = ['first_name', 'last_name', 'username', 'password']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('foldername','title', 'image', 'description')

class ImageFolderForm(forms.ModelForm):
    class Meta:
        model = ImageFolder
        fields = ['name']

class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ['name', 'logo']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'agency', 'abstract', 'period']
    
# Measurement Form
class MeasurementForm(forms.Form):
    stations = forms.ModelChoiceField(label="Station", help_text="Select a station", queryset=Station.objects.all(),

                                      widget=widgets.Select(attrs={'class': 'form-control'}))
    measurement_date = forms.DateField(label="Date", help_text="Enter the observation date",
                                       widget=widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    measurement_temp = forms.FloatField(label="Temperature", help_text="Enter the temperature in Celsius",
                                        widget=widgets.NumberInput(attrs={'class': 'form-control'}))
    measurement_precip = forms.FloatField(label="Precipitation", help_text="Enter the precipitation in mm",
                                          widget=widgets.NumberInput(attrs={'class': 'form-control'}))


# Station Form
class StationForm(forms.Form):
    station_id = forms.CharField(max_length=10)
    station_name = forms.CharField(max_length=100)
    station_lat = forms.FloatField()
    station_lon = forms.FloatField()
    station_elev = forms.FloatField(required=False)
    station_location = forms.CharField(max_length=100, required=False)
    station_organization = forms.CharField(max_length=10)
    station_year_established = forms.IntegerField(required=False)


""" # Organization Form
class OrganizationForm(forms.Form):
    organization_id = forms.CharField(max_length=10)
    organization_name = forms.CharField(max_length=100)
    organization_address = forms.CharField(max_length=100, required=False)
    organization_city = forms.CharField(max_length=100, required=False)
    organization_country = forms.CharField(max_length=2, required=False)
 """

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, required=False)
    institution = forms.CharField(max_length=100)
    query = forms.CharField(widget=forms.Textarea)