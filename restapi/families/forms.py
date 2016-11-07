from django import forms
from families.models import Familia, Persona


class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ('nombre', 'pais')


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'edad', 'familia')
