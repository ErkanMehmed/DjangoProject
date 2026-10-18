from django import forms

from manufacturers.models import Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country', 'founded_year', 'logo_url', 'description']
        labels = {
            'name': 'Manufacturer name',
            'country': 'Manufacturer country',
            'founded_year': 'Manufacturer founded year',
            'logo_url': 'Manufacturer logo url',
            'description': 'Manufacturer description',
        }
        help_texts = {
            'logo_url': 'Paste a manufacturer logo url',
            'founded_year': 'The year must be between 1800 and current year',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter manufacturer name'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country'}),
        }
        error_messages = {
            'name': {
                'required': 'You need to enter manufacturer name', 'unique': 'A manufacturer with this name already exists.',},
            'country': {
                'required': 'You need to enter manufacturer country',
            },
            'founded_year': {
                'required': 'You need to enter manufacturer founded year',
            }
        }

class ManufacturerCreateForm(ManufacturerForm):
    ...
class ManufacturerUpdateForm(ManufacturerForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True