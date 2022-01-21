import json
from django.shortcuts import render
from django.http.response import JsonResponse


DB = []


def home(request):
    return render(request, 'poll.html')


def msg(request):
    data = request.GET.get('msg')
    DB.append(data)
    return JsonResponse({'result': True})


def get_msg(request):
    length = int(request.GET.get('length', 0))
    data = {
        'content': json.dumps(DB[length:], ensure_ascii=False),
        'max_length': len(DB)
    }
    return JsonResponse(data)
