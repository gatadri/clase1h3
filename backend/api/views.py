import requests
from django.http import JsonResponse

def obtener_posts(request):
    url = "https://picsum.photos/v2/list"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data, safe=False)