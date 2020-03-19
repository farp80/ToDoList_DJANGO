from .models import Notes
from django import forms


class NotesModelForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'due_date', 'label')
