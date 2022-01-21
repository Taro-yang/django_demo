from django.shortcuts import render
from django.http.response import JsonResponse
import queue

# 使用全局变量，生产环境可更换为redis等消息队列
USER = {}


def home(request):
    uid = request.GET.get('uid')
    USER[uid] = queue.Queue()
    return render(request, 'long_poll.html', {'uid': uid})


def msg(request):
    txt = request.GET.get('msg')
    for que in USER.values():
        que.put(txt)
    return JsonResponse({'result': True})


def get_msg(request):
    uid = request.GET.get('uid')
    que = USER[uid]
    data = {
        'result': True,
        'data': None,
    }
    try:
        msg = que.get(timeout=20)
        data['data'] = msg
    except:
        data['result'] = False
    return JsonResponse(data)
