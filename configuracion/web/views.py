from django.shortcuts import render
from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formularioPacientes import FormularioPacientes
from web.models import Medicos
from web.models import Pacientes

# Create your views here.
#Render es PINTAR 
def Home(request):
    return render(request, 'index.html')

def MedicosVista(request):

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
            
            ##LLevar datos hacia la BD
            ##Objeto de la clase medicos
            medicoNuevo=Medicos(
                nombres=datos["nombre"], 
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tarjeta=datos["tarjeta_Profesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"], 
            )
            medicoNuevo.save()
            print("Datos guardados correctamente")
            


    return render(request, 'registrosmedicos.html', diccionario)
    


## Vista Pacientes
def PacientesVista(request):

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
            ##LLevar datos hacia la BD
            ##Objeto de la clase medicos
            pacienteNuevo=Pacientes(
                nombres= datos["nombre"],
                apellidos= datos["apellidos"],
                documento= datos["cedula"],
                regimen= datos["regimen"],
                grupoingreso= datos["grupo"],
                cuota= datos["cuota"],
                telefono= datos["telefono"],
                correo= datos["correo"],      
            )
            pacienteNuevo.save()
            print("Datos guardados correctamente")
            


    return render(request, 'registropacientes.html', diccionario)



