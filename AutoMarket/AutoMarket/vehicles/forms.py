from django import forms

from vehicles.models import Vehicle

from manufacturers.models import Manufacturer


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['manufacturer', 'model_name', 'year', 'price']
        widgets = {
            'manufacturer': forms.TextInput(attrs={'placeholder': 'Manufacturer'}),
            'model_name': forms.TextInput(attrs={'placeholder': 'Enter model name'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Enter manufacturing year'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter vehicle price'}),
        }

        labels = {
            'manufacturer': 'Manufacturer',
            'model_name': 'Model Name',
            'year': 'Year',
            'price': 'Price',
        }

        help_texts = {
            'manufacturer': 'Select the vehicle manufacturer.',
            'model_name': 'Enter the vehicle model.',
            'year': 'Enter the year the vehicle was manufactured.',
            'price': 'Enter the price of the vehicle.',
        }

        error_messages = {
            'manufacturer': {
                'required': 'Please select a manufacturer.',
            },
            'model_name': {
                'required': 'Please select a model name.',
                'max_length': 'The model name is too long.',
            },
            'year': {
                'required': 'Please select a year.',
                'invalid': 'Please enter a valid year.',
            },
            'price': {
                'required': 'Please enter the vehicle price.',
                'invalid': 'Please enter the valid price of the vehicle.',
            }
        }

class VehicleCreateForm(VehicleForm):
    pass

class VehicleUpdateForm(VehicleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['manufacturer'].disabled = True

class VehicleFilterForm(forms.Form):
    SORT_CHOICES = [
        ('year', 'The newest'),
        ('manufacturer', 'Manufacturer A-Z'),
    ]

    q = forms.CharField(required=True, label='Search', widget=forms.TextInput(attrs={'placeholder': 'Search by manufacturer'}))
    manufacturers = forms.ModelChoiceField(queryset=Manufacturer.objects.all(), required=False, empty_label='Select manufacturer')
    max_price = forms.IntegerField(required=False, min_value=1, label='Max price')
    sort = forms.ChoiceField(required=False, choices=SORT_CHOICES)
