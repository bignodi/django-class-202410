from django import forms

from todo.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name",)
