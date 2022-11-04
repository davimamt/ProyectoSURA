
from django import forms 
class FormularioMedico(forms.Form):

    ESPECIALIDADES = (
        (1, 'Cardiología'),
        (2, 'Medicina Interna'),
        (3, 'Medico General'),
        (4, 'Ortopedia'),
        (5, 'Pediatria'),
    )
    JORNADAS = (
        (1, '6:00 - 14:00'),
        (2, '14:00 - 22:00'),
        (3, '22:00 - 6:00'),

    )
    SEDES = (
        (1, 'Almacentro'),
        (2, 'Punto Clave'),
        (3, 'Molinos'),

    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15

    )
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15
    )
    cedula = forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=10


    )
    tarjeta_Profesional = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20
    )
    especialidad = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices= ESPECIALIDADES
    )
    jornada = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices= JORNADAS


    )
    contacto = forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20

    )
    sede = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices= SEDES
    )
