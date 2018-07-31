from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def note_list(request):
    notes = Note.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'note/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'note/note_detail.html', {'note':note})

def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.published_date = timezone.now()
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'note/note_edit.html', {'form': form})

def note_edit(request, pk):
    note  =get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.published_date = timezone.now()
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/note_edit.html', {'form': form})


