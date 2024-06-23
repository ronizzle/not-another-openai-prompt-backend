from django.http import JsonResponse
from .prompts import generate_openai_answer

def generate_answer(request):
    question = request.GET.get('question')
    answer = generate_openai_answer(question)
    return JsonResponse({'answer': answer})