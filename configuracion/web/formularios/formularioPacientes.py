from django import forms 
class FormularioPacientes(forms.Form):

   
    
    REGIMEN = (
        (1, 'Contributivo'),
        (2, 'Subsidiado'), 
    )
    
    GRUPO = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C'), 
    )
    
    
    CUOTA = (
        (1, 'Nivel A: $3.700'),
        (2, 'Nivel B: $14.700'),
        (3, 'Nivel C: $38.500'),
    
    
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
    
    regimen = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices= REGIMEN
    )
    
    grupo = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices= GRUPO
    )
    
    cuota = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices= CUOTA
    )
    
    telefono = forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20

    )
    
    correo = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15
    )