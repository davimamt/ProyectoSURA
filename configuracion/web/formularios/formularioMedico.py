
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

    nombre = forms.CharField()
    apellidos = forms.CharField()
    cedula = forms.CharField()
    tarjetaProfesional = forms.CharField()
    especialidad = forms.ChoiceField()
    jornada = forms.ChoiceField()
    contacto = forms.CharField()
    sede = forms.ChoiceField()
