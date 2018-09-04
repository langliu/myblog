from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads


@csrf_exempt
def login(request):
    if request.method == 'POST':
        request_data = loads(request.body)
        print(request_data)
        if request_data['name'] == 'allen' and request_data['password'] == '123456':
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
