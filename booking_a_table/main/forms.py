from .models import RentATable
from django.forms import ModelForm, TextInput, NumberInput, DateInput, TimeInput


class RentATableForm(ModelForm):
    class Meta:
        model = RentATable
        fields = ['client_name', 'clients_count', 'date', 'time', 'phone_number']

        widgets = {
            "client_name": TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Например: Иван/Ольга'
            }),
            "clients_count": NumberInput(attrs={
                'type': 'range',
                'value': "1",
                'min': "1",
                'max': "16",
                'oninput': "rangevalue.value=value"
            }),
            "date": DateInput(attrs={
                'type': 'date',
                'class': 'text-input',
                'placeholder': 'Например: 25.12.2022'
            }),
            "time": TimeInput(attrs={
                'type': 'time',
                'class': 'text-input',
                'placeholder': 'Например: 16:00'
            }),
            "phone_number": TextInput(attrs={
                'id': "phone",
                'class': "text-input phone",
                'placeholder': "+7(999)999-99-99"
            })
        }
