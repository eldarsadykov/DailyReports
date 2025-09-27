from django import forms
from django.core.exceptions import ValidationError

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
            'step': 5,
        })
    )

    def clean_key(self):
        key = self.cleaned_data['key']
        if Task.objects.filter(user=self.initial.get('user'), key=key).exists():
            raise ValidationError('Task key already exists.')
        return key

    class Meta:
        model = Task
        fields = ['key', 'name', 'progress']
