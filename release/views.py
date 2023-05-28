from django.http import HttpResponse
import socket

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    res = """Hello, This is v1 release!<br>
    Machine IP Address: {local_ip}<br>
    Your IP Address: {client_ip}""".format(local_ip=local_ip, client_ip=get_client_ip(request))
    return HttpResponse(res)