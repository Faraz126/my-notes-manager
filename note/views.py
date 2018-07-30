from django.shortcuts import render
from .models import Note
from django.utils import timezone
# Create your views here.

def note_list(request):
    notes = Note.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'note/note_list.html', {'notes': notes})