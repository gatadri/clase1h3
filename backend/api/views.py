import requests
from django.http import JsonResponse

def obtener_posts(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data, safe=False)