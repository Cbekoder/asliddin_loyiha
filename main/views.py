from django.shortcuts import render
from .utils import get_score

def home(request):
    text=request.POST.get('matn') 
    context={
        "res":get_score(text),
        "text":text}
    return render(request, 'index.html', context)


