from django.shortcuts import render
from django.db.models import Q
from main.models import ScoreEntry

def home(request):
    text = request.POST.get('matn', '').strip()  

    score = None 
    if text:
        entry = ScoreEntry.objects.filter(Q(text=text) | Q(text__icontains=text)).first()
        if entry:
            score = entry.score 

    context = {
        "res": score,
        "text": text
    }
    return render(request, 'index.html', context)
