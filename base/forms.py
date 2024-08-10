from django.forms import ModelForm
from .models import Task, Tasklist

class TasklistForm(ModelForm):
    class Meta:
        model = Tasklist
        fields = '__all__'
