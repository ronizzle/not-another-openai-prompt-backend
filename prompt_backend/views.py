from django.http import JsonResponse, StreamingHttpResponse
from .prompts import generate_openai_answer, generate_realtime_openai_answer

def generate_answer(request):
    question = request.GET.get('question')
    answer = generate_openai_answer(question)
    return JsonResponse({'answer': answer})

def generate_answer_realtime(request):
    question = request.GET.get('question')
    return StreamingHttpResponse(generate_realtime_openai_answer(question), content_type='text/event-stream')