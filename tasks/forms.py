from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    classString = 'input input-bordered w-full'

    key = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': classString,
            'placeholder': 'Task Key'})
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': classString,
            'placeholder': 'Task Name'})
    )

    progress = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': classString,
            'placeholder': 'Task Progress',
            'value': 0,
            'min': 0,
            'max': 100,
        })
    )

    class Meta:
        model = Task
        fields = ['key', 'name', 'progress']
