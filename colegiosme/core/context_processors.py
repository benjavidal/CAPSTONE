from .models import EstadoMensaje

def Mensaje_no_leidos(request):
    if request.user.is_authenticated:
        
        contador_mensajes_no_leidos = EstadoMensaje.objects.filter(destinatario=request.user, leido=False).count()
        print(contador_mensajes_no_leidos)
        return {'mensaje_no_leidos': contador_mensajes_no_leidos}
    return {}
