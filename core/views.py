from django.http import JsonResponse
from .tasks import square_number


def square_view(request):
    x = int(request.GET.get("x", 2))
    task = square_number.delay(x)
    return JsonResponse({"task_id": task.id, "status": "Task started!"})
