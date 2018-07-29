from django.shortcuts import render

# Create your views here.

def note_list(request):
    return render(request, 'note/note_list.html', {})