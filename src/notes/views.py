from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from .forms import NotesModelForm

# Create your views here.


def note_list_view(request):
    form = NotesModelForm()
    if request.method == 'POST':
        print("$$$$")
        form = NotesModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('note-list')

    to_do_list = Notes.objects.filter(finished=False)
    print(len(to_do_list))
    completed_do_list = Notes.objects.filter(finished=True)
    context = {
        "to_do_list": to_do_list,
        "completed_list": completed_do_list,
        "form": form
    }
    return render(request, "note_list.html", context)


def finished_item(request, id):
    note = get_object_or_404(Notes, id=id)
    note.finished = True
    note.save()
    return redirect('note-list')


def delete_item(request, id):
    note = get_object_or_404(Notes, id=id)
    note.delete()
    return redirect('note-list')


def recover_item(request, id):
    note = get_object_or_404(Notes, id=id)
    note.finished = False
    note.save()
    return redirect('note-list')
