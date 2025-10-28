from django import forms
from django.core.exceptions import ValidationError

from tasks.models import Task


class TaskForm(forms.ModelForm):
    classString = 'input input-bordered w-full mb-4'

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

    url = forms.URLField(
        widget=forms.TextInput(attrs={
            'class': classString,
            'placeholder': 'URL'})
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
            raise ValidationError('Task with this Key already exists for this User.')
        return key

    class Meta:
        model = Task
        fields = ['key', 'name', 'url', 'progress']
