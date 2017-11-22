from django import forms
from hotel_app.models import Resident

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident

        # acá van los campos del modelo que vamos a usar
        fields = [
            'name',
            'surname',
            'email',
        ]
        # label que acompaña al input
        labels = {
            'name': 'Nombre * ',
            'surname': 'Apellido * ',
            'email': 'E-mail * ',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }