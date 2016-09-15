from django.forms import ModelForm
from updates.models import loadStatus

class updateForm(ModelForm):
    class Meta:
        model = loadStatus
        fields = ['load_num', 'location', 'carrier']
