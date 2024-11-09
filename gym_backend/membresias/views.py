from django.contrib.auth import login
from django.http import JsonResponse
from .models import Clientes

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Buscar el cliente por nombre de usuario
            cliente = Clientes.objects.get(nombre=username)
            c =Clientes.objects.get(password=password)
            # Verificar la contraseña
            if cliente!=None and c!=None:
                # Iniciar sesión del cliente
                login(request, cliente)

                # Devolver la información del cliente en formato JSON
                return JsonResponse({
                    'id': cliente.idcliente,
                    'nombre': cliente.nombre,
                    'correo': cliente.correo,
                    'fecha': cliente.fecha.isoformat(),
                    'idmember': cliente.idmember.id
                })
            else:
                return JsonResponse({'error': 'Credenciales inválidas'}, status=401)
        except Clientes.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método HTTP no permitido'}, status=405)