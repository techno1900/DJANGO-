from django.forms import ModelForm
from . models import contectTable

class contactForm(ModelForm):
    class Meta():
        model = contectTable
        fields = '__all__'