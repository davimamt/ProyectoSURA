from django.shortcuts import render

# Create your views here.
#Render es PINTAR 
def Home(request):
    return render(request, 'index.html') 
