from django.shortcuts import render
from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formularioPacientes import FormularioPacientes


# Create your views here.
#Render es PINTAR 
def Home(request):
    return render(request, 'index.html')

def Medicos(request):

    # DEBO UTILIZAR LA CLASE formularioMedico
    # Se debe crear un objeto 
    formulario = FormularioMedico()
    diccionario = {
        "formulario": formulario
    }

    #Activar la recepcion de datos
    if request.method == 'POST':
        #VALIDAR SI LOS DATOS SON CORRECTOS
        datosRecibidos = FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            print(datos)


    return render(request, 'registrosmedicos.html', diccionario)
    

def Pacientes(request):

    # DEBO UTILIZAR LA CLASE formularioMedico
    # Se debe crear un objeto 
    formulario = FormularioPacientes()
    diccionario = {
        "formulario": formulario
    }

    #Activar la recepcion de datos
    if request.method == 'POST':
        #VALIDAR SI LOS DATOS SON CORRECTOS
        datosRecibidos = FormularioPacientes(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            print(datos)


    return render(request, 'registropacientes.html', diccionario)



